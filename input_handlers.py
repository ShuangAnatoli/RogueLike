from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Optional, Tuple, Union
import os
import tcod

from actions import Action, BumpAction, PickupAction, WaitAction
import actions
import color
import exceptions
import random
import sys
import numpy as np
import pandas as pd
from pathlib import Path

# As PosixPath
sys.path.append(str(Path(__file__).parent / "components"))
import equippable

if TYPE_CHECKING:
    from engine import Engine
    from entity import Item


MOVE_KEYS = {
    # Arrow keys.
    tcod.event.KeySym.UP: (0, -1),
    tcod.event.KeySym.DOWN: (0, 1),
    tcod.event.KeySym.LEFT: (-1, 0),
    tcod.event.KeySym.RIGHT: (1, 0),
    tcod.event.KeySym.HOME: (-1, -1),
    tcod.event.KeySym.END: (-1, 1),
    tcod.event.KeySym.PAGEUP: (1, -1),
    tcod.event.KeySym.PAGEDOWN: (1, 1),
    # Numpad keys.
    tcod.event.KeySym.KP_1: (-1, 1),
    tcod.event.KeySym.KP_2: (0, 1),
    tcod.event.KeySym.KP_3: (1, 1),
    tcod.event.KeySym.KP_4: (-1, 0),
    tcod.event.KeySym.KP_6: (1, 0),
    tcod.event.KeySym.KP_7: (-1, -1),
    tcod.event.KeySym.KP_8: (0, -1),
    tcod.event.KeySym.KP_9: (1, -1),
    # Vi keys.
    tcod.event.KeySym.h: (-1, 0),
    tcod.event.KeySym.j: (0, 1),
    tcod.event.KeySym.k: (0, -1),
    tcod.event.KeySym.l: (1, 0),
    tcod.event.KeySym.y: (-1, -1),
    tcod.event.KeySym.u: (1, -1),
    tcod.event.KeySym.b: (-1, 1),
    tcod.event.KeySym.n: (1, 1),
}

WAIT_KEYS = {
    tcod.event.KeySym.PERIOD,
    tcod.event.KeySym.KP_5,
    tcod.event.KeySym.CLEAR,
}

CONFIRM_KEYS = {
    tcod.event.KeySym.RETURN,
    tcod.event.KeySym.KP_ENTER,
}

ActionOrHandler = Union[Action, "BaseEventHandler"]
"""An event handler return value which can trigger an action or switch active handlers.

If a handler is returned then it will become the active handler for future events.
If an action is returned it will be attempted and if it's valid then
MainGameEventHandler will become the active handler.
"""


class BaseEventHandler(tcod.event.EventDispatch[ActionOrHandler]):
    def handle_events(self, event: tcod.event.Event) -> BaseEventHandler:
        """Handle an event and return the next active event handler."""
        state = self.dispatch(event)
        if isinstance(state, BaseEventHandler):
            return state
        assert not isinstance(state, Action), f"{self!r} can not handle actions."
        return self

    def on_render(self, console: tcod.Console) -> None:
        raise NotImplementedError()

    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()


class PopupMessage(BaseEventHandler):
    """Display a popup text window."""

    def __init__(self, parent_handler: BaseEventHandler, text: str):
        self.parent = parent_handler
        self.text = text

    def on_render(self, console: tcod.Console) -> None:
        """Render the parent and dim the result, then print the message on top."""
        self.parent.on_render(console)
        console.tiles_rgb["fg"] //= 8
        console.tiles_rgb["bg"] //= 8

        console.print(
            console.width // 2,
            console.height // 2,
            self.text,
            fg=color.white,
            bg=color.black,
            alignment=tcod.CENTER,
        )

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[BaseEventHandler]:
        """Any key returns to the parent handler."""
        return self.parent



class EventHandler(BaseEventHandler):
    def __init__(self, engine: Engine):
        self.engine = engine

    def handle_events(self, event: tcod.event.Event) -> BaseEventHandler:
        """Handle events for input handlers with an engine."""
        action_or_state = self.dispatch(event)
        if isinstance(action_or_state, BaseEventHandler):
            return action_or_state
        if self.handle_action(action_or_state):
            # A valid action was performed.
            if not self.engine.player.is_alive:
                # The player was killed sometime during or after the action.
                return GameOverEventHandler(self.engine)
            elif self.engine.player.level.requires_level_up:
                return LevelUpEventHandler(self.engine)
            return MainGameEventHandler(self.engine)  # Return to the main handler.
        return self

    def handle_action(self, action: Optional[Action]) -> bool:
        """Handle actions returned from event methods.

        Returns True if the action will advance a turn.
        """
        if action is None:
            return False

        try:
            action.perform()
        except exceptions.Impossible as exc:
            self.engine.message_log.add_message(exc.args[0], color.impossible)
            return False  # Skip enemy turn on exceptions.

        self.engine.handle_enemy_turns()

        self.engine.update_fov()
        return True

    def ev_mousemotion(self, event: tcod.event.MouseMotion) -> None:
        if self.engine.game_map.in_bounds(event.tile.x, event.tile.y):
            self.engine.mouse_location = event.tile.x, event.tile.y

    def on_render(self, console: tcod.Console) -> None:
        self.engine.render(console)


class AskUserEventHandler(EventHandler):
    """Handles user input for actions which require special input."""

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        """By default any key exits this input handler."""
        if event.sym in {  # Ignore modifier keys.
            tcod.event.K_LSHIFT,
            tcod.event.K_RSHIFT,
            tcod.event.K_LCTRL,
            tcod.event.K_RCTRL,
            tcod.event.K_LALT,
            tcod.event.K_RALT,
            tcod.event.K_LGUI,
            tcod.event.K_RGUI,
            tcod.event.K_MODE,
        }:
            return None
        return self.on_exit()

    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[ActionOrHandler]:
        """By default any mouse click exits this input handler."""
        return self.on_exit()

    def on_exit(self) -> Optional[ActionOrHandler]:
        """Called when the user is trying to exit or cancel an action.

        By default this returns to the main event handler.
        """
        return MainGameEventHandler(self.engine)


class CharacterScreenEventHandler(AskUserEventHandler):
    TITLE = "Character Information"

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        if self.engine.player.x <= 30:
            x = 40
        else:
            x = 0

        y = 0

        width = len(self.TITLE) + 4

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=7,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0),
        )

        console.print(x=x + 1, y=y + 1, string=f"Level: {self.engine.player.level.current_level}")
        console.print(x=x + 1, y=y + 2, string=f"XP: {self.engine.player.level.current_xp}")
        console.print(
            x=x + 1,
            y=y + 3,
            string=f"XP for next Level: {self.engine.player.level.experience_to_next_level}",
        )

        console.print(x=x + 1, y=y + 4, string=f"Attack: {self.engine.player.fighter.power}")
        console.print(x=x + 1, y=y + 5, string=f"Defense: {self.engine.player.fighter.defense}")


class LevelUpEventHandler(AskUserEventHandler):
    TITLE = "Level Up"

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)

        if self.engine.player.x <= 30:
            x = 40
        else:
            x = 0

        console.draw_frame(
            x=x,
            y=0,
            width=35,
            height=8,
            title=self.TITLE,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0),
        )

        console.print(x=x + 1, y=1, string="Congratulations! You level up!")
        console.print(x=x + 1, y=2, string="Select an attribute to increase.")

        console.print(
            x=x + 1,
            y=4,
            string=f"a) Constitution (+20 HP, from {self.engine.player.fighter.max_hp})",
        )
        console.print(
            x=x + 1,
            y=5,
            string=f"b) Strength (+1 attack, from {self.engine.player.fighter.power})",
        )
        console.print(
            x=x + 1,
            y=6,
            string=f"c) Agility (+1 defense, from {self.engine.player.fighter.defense})",
        )

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        player = self.engine.player
        key = event.sym
        index = key - tcod.event.K_a

        if 0 <= index <= 2:
            if index == 0:
                player.level.increase_max_hp()
            elif index == 1:
                player.level.increase_power()
            else:
                player.level.increase_defense()
        else:
            self.engine.message_log.add_message("Invalid entry.", color.invalid)

            return None

        return super().ev_keydown(event)

    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[ActionOrHandler]:
        """
        Don't allow the player to click to exit the menu, like normal.
        """
        return None


class InventoryEventHandler(AskUserEventHandler):
    """This handler lets the user select an item.

    What happens then depends on the subclass.
    """

    TITLE = "<missing title>"

    def on_render(self, console: tcod.Console) -> None:
        """Render an inventory menu, which displays the items in the inventory, and the letter to select them.
        Will move to a different position based on where the player is located, so the player can always see where
        they are.
        """
        super().on_render(console)
        number_of_items_in_inventory = len(self.engine.player.inventory.items)

        height = number_of_items_in_inventory + 2

        if height <= 3:
            height = 3

        if self.engine.player.x <= 30:
            x = 40
        else:
            x = 0

        y = 0

        width = len(self.TITLE) + 4

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=height,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0),
        )
        console.print(x + 1, y, f" {self.TITLE} ", fg=(0, 0, 0), bg=(255, 255, 255))

        if number_of_items_in_inventory > 0:
            for i, item in enumerate(self.engine.player.inventory.items):
                item_key = chr(ord("a") + i)

                is_equipped = self.engine.player.equipment.item_is_equipped(item)

                item_string = f"({item_key}) {item.name}"

                if is_equipped:
                    item_string = f"{item_string} (E)"

                console.print(x + 1, y + i + 1, item_string)
        else:
            console.print(x + 1, y + 1, "(Empty)")

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        player = self.engine.player
        key = event.sym
        index = key - tcod.event.K_a

        if 0 <= index <= 26:
            try:
                selected_item = player.inventory.items[index]
            except IndexError:
                self.engine.message_log.add_message("Invalid entry.", color.invalid)
                return None
            return self.on_item_selected(selected_item)
        return super().ev_keydown(event)

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        raise NotImplementedError()


class InventoryActivateHandler(InventoryEventHandler):
    """Handle using an inventory item."""

    TITLE = "Select an item to use"

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        if item.consumable:
            # Return the action for the selected item.
            return item.consumable.get_action(self.engine.player)
        elif item.equippable:
            return actions.EquipAction(self.engine.player, item)
        else:
            return None


class InventoryDropHandler(InventoryEventHandler):
    """Handle dropping an inventory item."""

    TITLE = "Select an item to drop"

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Drop this item."""
        return actions.DropItem(self.engine.player, item)


class SelectIndexHandler(AskUserEventHandler):
    """Handles asking the user for an index on the map."""

    def __init__(self, engine: Engine):
        """Sets the cursor to the player when this handler is constructed."""
        super().__init__(engine)
        player = self.engine.player
        engine.mouse_location = player.x, player.y

    def on_render(self, console: tcod.Console) -> None:
        """Highlight the tile under the cursor."""
        super().on_render(console)
        x, y = self.engine.mouse_location
        console.tiles_rgb["bg"][x, y] = color.white
        console.tiles_rgb["fg"][x, y] = color.black

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        """Check for key movement or confirmation keys."""
        key = event.sym
        if key in MOVE_KEYS:
            modifier = 1  # Holding modifier keys will speed up key movement.
            if event.mod & (tcod.event.KMOD_LSHIFT | tcod.event.KMOD_RSHIFT):
                modifier *= 5
            if event.mod & (tcod.event.KMOD_LCTRL | tcod.event.KMOD_RCTRL):
                modifier *= 10
            if event.mod & (tcod.event.KMOD_LALT | tcod.event.KMOD_RALT):
                modifier *= 20

            x, y = self.engine.mouse_location
            dx, dy = MOVE_KEYS[key]
            x += dx * modifier
            y += dy * modifier
            # Clamp the cursor index to the map size.
            x = max(0, min(x, self.engine.game_map.width - 1))
            y = max(0, min(y, self.engine.game_map.height - 1))
            self.engine.mouse_location = x, y
            return None
        elif key in CONFIRM_KEYS:
            return self.on_index_selected(*self.engine.mouse_location)
        return super().ev_keydown(event)

    def ev_mousebuttondown(self, event: tcod.event.MouseButtonDown) -> Optional[ActionOrHandler]:
        """Left click confirms a selection."""
        if self.engine.game_map.in_bounds(*event.tile):
            if event.button == 1:
                return self.on_index_selected(*event.tile)
        return super().ev_mousebuttondown(event)

    def on_index_selected(self, x: int, y: int) -> Optional[ActionOrHandler]:
        """Called when an index is selected."""
        raise NotImplementedError()


class LookHandler(SelectIndexHandler):
    """Lets the player look around using the keyboard."""

    def on_index_selected(self, x: int, y: int) -> MainGameEventHandler:
        """Return to main handler."""
        return MainGameEventHandler(self.engine)


class SingleRangedAttackHandler(SelectIndexHandler):
    """Handles targeting a single enemy. Only the enemy selected will be affected."""

    def __init__(self, engine: Engine, callback: Callable[[Tuple[int, int]], Optional[Action]]):
        super().__init__(engine)

        self.callback = callback

    def on_index_selected(self, x: int, y: int) -> Optional[Action]:
        return self.callback((x, y))


class AreaRangedAttackHandler(SelectIndexHandler):
    """Handles targeting an area within a given radius. Any entity within the area will be affected."""

    def __init__(
        self,
        engine: Engine,
        radius: int,
        callback: Callable[[Tuple[int, int]], Optional[Action]],
    ):
        super().__init__(engine)

        self.radius = radius
        self.callback = callback

    def on_render(self, console: tcod.Console) -> None:
        """Highlight the tile under the cursor."""
        super().on_render(console)

        x, y = self.engine.mouse_location

        # Draw a rectangle around the targeted area, so the player can see the affected tiles.
        console.draw_frame(
            x=x - self.radius - 1,
            y=y - self.radius - 1,
            width=self.radius ** 2,
            height=self.radius ** 2,
            fg=color.red,
            clear=False,
        )

    def on_index_selected(self, x: int, y: int) -> Optional[Action]:
        return self.callback((x, y))


class CraftingMenuHandler(AskUserEventHandler):

    def __init__(self, engine: Engine, time_left = 112, location = 4):
        self.time_left = time_left
        self.location = location
        self.engine = engine


        self.materials_list = ['nomex_socks', 'boots_combat', 'boots_steel', 'boots_bunker', 'boots_hiking', 'boots', 'felt_patch', 'bag_plastic', 'hat_ball', 'hat_boonie', 'glasses_safety', 'glasses_bal', 'mask_filter', 'goggles_ski', 'helmet_liner',
                  'steel', 'steel', 'copper_scrap_equivalent', 'steel', 'nail', 'scrap_bronze', 'medical_tape', 'superglue',  'cooking_oil', 'lamp_oil', 'motor_oil', 'water', 'water_clean', 'vinegar', 'salt',
                  'string', 'string', 'any_tallow', 'wax', 'leather', 'chitin_piece', 'fur', 'cured_pelt', 'cured_hide', 'acidchitin_piece',
                  'string', 'string', 'cordage_short', 'birchbark', 'straw_pile', 'cordage_superior', 'rock', 'sword_wood', 'pointy_stick', 'long_pole', 'log', 'stick_long', 'cordage' ,
                  '2x4', 'rag', 'string', 'string', 'neoprene', 'plastic_chunk', 'fur','sheet_metal_small', 'paper', 'duct_tape', 'scrap', 'link_sheet', 'chain_link', 'wire', 'filament', 'pipe', 'rebar', 'spike']


        
    TITLE = ""
    
    def on_render(self, console: tcod.Console) -> None:
        """Creates a downtime menu for the player to select locations to craft with. Sends to stairs currently; TODO: send to crafting menu instead
        """

        player = self.engine.player
        

        armorData = pd.read_csv("armor.csv")
        weaponData = pd.read_csv("weapon.csv")

        valid_armor_names = []
        for row in armorData.rows:
            craftable = True
            recipe = row["recipe"]
            for mat_options in recipe:
                mat_satisfied = False
                for mat_tuple in mat_options:
                    material = mat_tuple[0]
                    mat_quantity = mat_tuple[1]
                    for i, mat_name in enumerate(self.materials_list):
                        if mat_name == material:
                            if player.inventory.materials[i] >= mat_quantity:
                                mat_satisfied = True
                if mat_satisfied == False:
                    craftable = False
            if craftable:
                valid_armor_names.append(row["name"]["str"])


        
        super().on_render(console)
        

        height = 18
        x = 0
        y = 0

        width = 70

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=height,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0),
        )
        self.TITLE = f"Crafting: {self.time_left} hours left"

        console.print(x + 1, y, f" {self.TITLE} ", fg=(0, 0, 0), bg=(255, 255, 255))
        locations = ["(a) Residential District: Mingle - clothing components", "(b) Residential District: Game - metal, trade goods, d4 x dex gold", 
                     "(c) Woodlands: Hunt - hide and chitin", "(d) Woodlands: Gather - natural materials",
                    "(e) Scrapyard: Scavenge - scrap", "(f) Scrapyard: Labor - d6 x strength gold", 
                     "(g) Market: Shop - spend 20 gold, many random mats", "(h) Market: Steal - dex based random"]
        
        for i, item in enumerate(locations):
            console.print(x + 1, y + i + 1, item)

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
       
        player = self.engine.player
        locations = ["(a) Residential District: Mingle - clothing components", "(b) Residential District: Game - metal, trade goods, d4 x dex gold", 
                     "(c) Woodlands: Hunt - hide and chitin", "(d) Woodlands: Gather - natural materials",
                    "(e) Scrapyard: Scavenge - scrap", "(f) Scrapyard: Labor - d6 x strength gold", 
                     "(g) Market: Shop - spend 20 gold, many random mats", "(h) Market: Steal - dex based random"]
        
        player = self.engine.player
        key = event.sym
        index = key - tcod.event.K_a
        mat_mult = 5
        if 0 <= index <= 15:
            mat_list = self.materials_list
            if index == 0: 
                mat_list = ['nomex_socks', 'boots_combat', 'boots_steel', 'boots_bunker', 'boots_hiking', 'boots', 'felt_patch', 'bag_plastic', 'hat_ball', 'hat_boonie', 'glasses_safety', 'glasses_bal', 'mask_filter', 'goggles_ski', 'helmet_liner']
            elif index == 1: 
                mat_list = ['steel', 'steel', 'copper_scrap_equivalent', 'steel', 'nail', 'scrap_bronze', 'medical_tape', 'superglue',  'cooking_oil', 'lamp_oil', 'motor_oil', 'water', 'water_clean', 'vinegar', 'salt']
                mat_mult = 3
                gold_tally = 0
                for i in range(player.fighter.base_defense):
                    earnings = random.randint(1,4)
                    player.inventory.gold += earnings
                    gold_tally += earnings
                self.engine.message_log.add_message(f"You earned {gold_tally} gold.", color.gold)
            elif index == 2: 
                mat_list = ['string', 'string', 'any_tallow', 'wax', 'leather', 'chitin_piece', 'fur', 'cured_pelt', 'cured_hide', 'acidchitin_piece']
            elif index == 3: 
                mat_list = ['string', 'string', 'cordage_short', 'birchbark', 'straw_pile', 'cordage_superior', 'rock', 'sword_wood', 'pointy_stick', 'long_pole', 'log', 'stick_long', 'cordage' ]
            elif index == 4: 
                mat_list = ['2x4', 'rag', 'string', 'string', 'neoprene', 'plastic_chunk', 'fur','sheet_metal_small', 'paper', 'duct_tape', 'scrap', 'link_sheet', 'chain_link', 'wire', 'filament', 'pipe', 'rebar', 'spike']
            elif index == 5:
                gold_tally = 0
                for i in range(player.fighter.base_power):
                    earnings = random.randint(1,6)
                    player.inventory.gold += earnings
                    gold_tally += earnings
                self.engine.message_log.add_message(f"You earned {gold_tally} gold.", color.gold)
            elif index == 6:
                if player.inventory.gold > 20:
                    self.engine.message_log.add_message("Not enough gold.", color.invalid)
                    return None
                else:
                    player.inventory.gold -= 20
                    mat_mult = 10
            elif index == 6:
                mat_mult = 0
                for i in range(player.fighter.base_defense):
                    mat_mult += random.randint(1,4)
            mat_string = ""
            for i in range(mat_mult):
                mat_found = random.randint(0,len(mat_list)-1)
                for j, mat in enumerate(self.materials_list):
                    if mat_list[mat_found] == mat:
                        player.inventory.materials[j] += 1
                if i == mat_mult-1:
                    mat_string += f"and {mat_list[mat_found]}."
                else:
                    mat_string += f"{mat_list[mat_found]} ,"
            self.engine.message_log.add_message(f"You got: "+mat_string, color.gold)
            
            if self.time_left > 0:
                return actions.TakeStairsAction(player)
        return super().ev_keydown(event)

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        raise NotImplementedError()

class DowntimeMenuHandler(AskUserEventHandler):
    """This handler lets the user select from the downtime menu for the player to select locations to craft with. Sends to stairs currently;
    """

    TITLE = "Downtime"
    def __init__(self, time_left = 112, location = 4):
        self.time_left = time_left
        self.location = location
    
    def on_render(self, console: tcod.Console) -> None:
        """Creates a downtime menu for the player to select locations to craft with. Sends to stairs currently; TODO: send to crafting menu instead
        """
        super().on_render(console)
        

        height = 18
        x = 0
        y = 0

        width = 70

        console.draw_frame(
            x=x,
            y=y,
            width=width,
            height=height,
            clear=True,
            fg=(255, 255, 255),
            bg=(0, 0, 0),
        )
        console.print(x + 1, y, f" {self.TITLE} ", fg=(0, 0, 0), bg=(255, 255, 255))
        locations = ["(a) Residential District: Mingle (1 hr) - clothes/household/food items", "(b) Residential District: Game (2 hrs) - metal, trade goods, d4 x dex gold", 
                     "(c) Woodlands: Hunt (4 hrs) - hide, chitin, meat", "(d) Woodlands: Gather (1 hr) - natural materials",
                    "(e) Scrapyard: Scavenge (1 hr) - scrap", "(f) Scrapyard: Labor (4 hrs) - d6 x strength gold", 
                     "(g) Market: Shop (1 hr) - spend 20 gold, many random mats", "(h) Market: Steal (1 hr) - dex based random", 
                     "(i) Arena: Crafting (? hrs) - turn mats into gear", "(X) Arena: Next battle (quit downtime)"]
        
        for i, item in enumerate(locations):
            console.print(x + 1, y + i + 1, item)

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        materials_list = ['nomex_socks', 'boots_combat', 'boots_steel', 'boots_bunker', 'boots_hiking', 'boots', 'felt_patch', 'bag_plastic', 'hat_ball', 'hat_boonie', 'glasses_safety', 'glasses_bal', 'mask_filter', 'goggles_ski', 'helmet_liner',
                  'steel', 'steel', 'copper_scrap_equivalent', 'steel', 'nail', 'scrap_bronze', 'medical_tape', 'superglue',  'cooking_oil', 'lamp_oil', 'motor_oil', 'water', 'water_clean', 'vinegar', 'salt',
                  'string', 'string', 'any_tallow', 'wax', 'leather', 'chitin_piece', 'fur', 'cured_pelt', 'cured_hide', 'acidchitin_piece',
                  'string', 'string', 'cordage_short', 'birchbark', 'straw_pile', 'cordage_superior', 'rock', 'sword_wood', 'pointy_stick', 'long_pole', 'log', 'stick_long', 'cordage' ,
                  '2x4', 'rag', 'string', 'string', 'neoprene', 'plastic_chunk', 'fur','sheet_metal_small', 'paper', 'duct_tape', 'scrap', 'link_sheet', 'chain_link', 'wire', 'filament', 'pipe', 'rebar', 'spike']


        
        player = self.engine.player
        key = event.sym
        index = key - tcod.event.K_a
        mat_mult = 5
        travelcost = abs(self.location//2-index//2)
        actionarray = [2,2,4,1,2,1,4,1,0,0]
        actioncost = actionarray[index]
        
        if index == 9:
            if travelcost+actioncost > self.time_left:
                damage = 4-self.location//2+actioncost-self.time_left
                if damage > 0:
                    self.engine.message_log.add_message(f"You didn't have enough time, and took {damage} damage sprinting back to the arena!", color.red)
                    player.hp -= damage
            return actions.TakeStairsAction(player)
        if 0 <= index <= 7:
            
            if actioncost+travelcost > self.time_left:
                self.engine.message_log.add_message(f"You don't have enough time; pick something else, or try returning to the arena", color.red)
                self.engine.message_log.add_message(f"Travel time: {travelcost}, Action time: {actioncost}, Time left: {self.time_left}", color.red)
                
            mat_list = materials_list
            if index == 0:
                mat_list = ['nomex_socks', 'boots_combat', 'boots_steel', 'boots_bunker', 'boots_hiking', 'boots', 'felt_patch', 'bag_plastic', 'hat_ball', 'hat_boonie', 'glasses_safety', 'glasses_bal', 'mask_filter', 'goggles_ski', 'helmet_liner']
            elif index == 1: 
                mat_list = ['steel', 'steel', 'copper_scrap_equivalent', 'steel', 'nail', 'scrap_bronze', 'medical_tape', 'superglue',  'cooking_oil', 'lamp_oil', 'motor_oil', 'water', 'water_clean', 'vinegar', 'salt']
                mat_mult = 3
                gold_tally = 0
                for i in range(player.fighter.base_defense):
                    earnings = random.randint(1,4)
                    player.inventory.gold += earnings
                    gold_tally += earnings
                self.engine.message_log.add_message(f"You earned {gold_tally} gold.", color.gold)
            elif index == 2: 
                mat_list = ['string', 'string', 'any_tallow', 'wax', 'leather', 'chitin_piece', 'fur', 'cured_pelt', 'cured_hide', 'acidchitin_piece']
            elif index == 3: 
                mat_list = ['string', 'string', 'cordage_short', 'birchbark', 'straw_pile', 'cordage_superior', 'rock', 'sword_wood', 'pointy_stick', 'long_pole', 'log', 'stick_long', 'cordage' ]
            elif index == 4: 
                mat_list = ['2x4', 'rag', 'string', 'string', 'neoprene', 'plastic_chunk', 'fur','sheet_metal_small', 'paper', 'duct_tape', 'scrap', 'link_sheet', 'chain_link', 'wire', 'filament', 'pipe', 'rebar', 'spike']
            elif index == 5:
                gold_tally = 0
                for i in range(player.fighter.base_power):
                    earnings = random.randint(1,6)
                    player.inventory.gold += earnings
                    gold_tally += earnings
                self.engine.message_log.add_message(f"You earned {gold_tally} gold.", color.gold)
            elif index == 6:
                if player.inventory.gold > 20:
                    self.engine.message_log.add_message("Not enough gold.", color.invalid)
                    return None
                else:
                    player.inventory.gold -= 20
                    mat_mult = 10
            elif index == 7:
                mat_mult = 0
                for i in range(player.fighter.base_defense):
                    mat_mult += random.randint(1,4)
            
            mat_string = ""
            for i in range(mat_mult):
                mat_found = random.randint(0,len(mat_list)-1)
                for j, mat in enumerate(materials_list):
                    if mat_list[mat_found] == mat:
                        player.inventory.materials[j] += 1
                if i == mat_mult-1:
                    mat_string += f"and {mat_list[mat_found]}."
                else:
                    mat_string += f"{mat_list[mat_found]} ,"
            self.engine.message_log.add_message(f"You got: "+mat_string, color.gold)
            newtime = self.time_left-actioncost-travelcost
            return DowntimeMenuHandler(self.engine, time_left = newtime, location = index)
        
        elif index == 8: #I think we need this to loop keydown correctly; we can't return DonwtimeMenuHandler at the outer level
            return DowntimeMenuHandler(self.engine, time_left = self.time_left-actioncost-travelcost, location = index)

        
        return super().ev_keydown(event)

    def on_item_selected(self, item: Item) -> Optional[ActionOrHandler]:
        """Called when the user selects a valid item."""
        raise NotImplementedError()

class MainGameEventHandler(EventHandler):
    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[ActionOrHandler]:
        action: Optional[Action] = None

        key = event.sym
        modifier = event.mod

        player = self.engine.player

        if key == tcod.event.K_PERIOD and modifier & (tcod.event.KMOD_LSHIFT | tcod.event.KMOD_RSHIFT):
            return DowntimeMenuHandler(self.engine)

        if key in MOVE_KEYS:
            dx, dy = MOVE_KEYS[key]
            action = BumpAction(player, dx, dy)
        elif key in WAIT_KEYS:
            action = WaitAction(player)

        elif key == tcod.event.K_ESCAPE:
            raise SystemExit()
        elif key == tcod.event.K_v:
            return HistoryViewer(self.engine)

        elif key == tcod.event.K_g:
            action = PickupAction(player)

        elif key == tcod.event.K_i:
            return InventoryActivateHandler(self.engine)
        elif key == tcod.event.K_d:
            return InventoryDropHandler(self.engine)
        elif key == tcod.event.K_c:
            return CharacterScreenEventHandler(self.engine)
        elif key == tcod.event.K_SLASH:
            return LookHandler(self.engine)

        # No valid key was pressed
        return action


class GameOverEventHandler(EventHandler):
    def on_quit(self) -> None:
        """Handle exiting out of a finished game."""
        if os.path.exists("savegame.sav"):
            os.remove("savegame.sav")  # Deletes the active save file.
        raise exceptions.QuitWithoutSaving()  # Avoid saving a finished game.

    def ev_quit(self, event: tcod.event.Quit) -> None:
        self.on_quit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> None:
        if event.sym == tcod.event.K_ESCAPE:
            self.on_quit()


CURSOR_Y_KEYS = {
    tcod.event.KeySym.UP: -1,
    tcod.event.KeySym.DOWN: 1,
    tcod.event.KeySym.PAGEUP: -10,
    tcod.event.KeySym.PAGEDOWN: 10,
}


class HistoryViewer(EventHandler):
    """Print the history on a larger window which can be navigated."""

    def __init__(self, engine: Engine):
        super().__init__(engine)
        self.log_length = len(engine.message_log.messages)
        self.cursor = self.log_length - 1

    def on_render(self, console: tcod.Console) -> None:
        super().on_render(console)  # Draw the main state as the background.

        log_console = tcod.Console(console.width - 6, console.height - 6)

        # Draw a frame with a custom banner title.
        log_console.draw_frame(0, 0, log_console.width, log_console.height)
        log_console.print_box(0, 0, log_console.width, 1, "┤Message history├", alignment=tcod.CENTER)

        # Render the message log using the cursor parameter.
        self.engine.message_log.render_messages(
            log_console,
            1,
            1,
            log_console.width - 2,
            log_console.height - 2,
            self.engine.message_log.messages[: self.cursor + 1],
        )
        log_console.blit(console, 3, 3)

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[MainGameEventHandler]:
        # Fancy conditional movement to make it feel right.
        if event.sym in CURSOR_Y_KEYS:
            adjust = CURSOR_Y_KEYS[event.sym]
            if adjust < 0 and self.cursor == 0:
                # Only move from the top to the bottom when you're on the edge.
                self.cursor = self.log_length - 1
            elif adjust > 0 and self.cursor == self.log_length - 1:
                # Same with bottom to top movement.
                self.cursor = 0
            else:
                # Otherwise move while staying clamped to the bounds of the history log.
                self.cursor = max(0, min(self.cursor + adjust, self.log_length - 1))
        elif event.sym == tcod.event.K_HOME:
            self.cursor = 0  # Move directly to the top message.
        elif event.sym == tcod.event.K_END:
            self.cursor = self.log_length - 1  # Move directly to the last message.
        else:  # Any other key moves back to the main game state.
            return MainGameEventHandler(self.engine)
        return None
