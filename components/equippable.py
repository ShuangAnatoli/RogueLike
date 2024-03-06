from __future__ import annotations

from typing import TYPE_CHECKING

import sys
sys.path.append('../tcod_tutorial_v2')
from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item


class Equippable(BaseComponent):
    parent: Item

    def __init__(
        self,
        equipment_type: EquipmentType,
        power_bonus: int = 0,
        defense_bonus: int = 0,
        attack_bonus: int = 0,
        armor_bonus: int = 0
    ):
        self.equipment_type = equipment_type

        self.power_bonus = power_bonus
        self.attack_bonus = attack_bonus
        self.armor_bonus = armor_bonus
        self.defense_bonus = defense_bonus


class Dagger(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=2, attack_bonus=1)


class Sword(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=4, attack_bonus=0)


class LeatherArmor(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=1, armor_bonus=3)


class ChainMail(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=3, armor_bonus=6)

class war_flail(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=6, attack_bonus = -3) 

class peasant_flail(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 0) 

class blackjack(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=3, attack_bonus = 6) 

class bokken(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=5, attack_bonus = 5) 

class barbed_wire_bat(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 6) 

class cudgel(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=2, attack_bonus = 6) 

class homewrecker(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=6, attack_bonus = -1) 

class ironshod_quarterstaff(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=5, attack_bonus = 5) 

class lucerne_hammer(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=9, attack_bonus = 0) 

class mace(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 4) 

class makeshift_sap(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=3, attack_bonus = 6) 

class morningstar(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=8, attack_bonus = 2) 

class nail_bat(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=6, attack_bonus = 6) 

class nailboard(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=2, attack_bonus = 4) 

class quarterstaff(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 5) 

class rock_in_a_sock(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=2, attack_bonus = 3) 

class shillelagh(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=5, attack_bonus = 5) 

class loaded_stick(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=6, attack_bonus = 5) 

class powered_quarterstaff(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 3) 

class tactical_tonfa_(off)(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 4) 

class tonfa(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 6) 

class wooden_tonfa(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 5) 

class war_hammer(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=8, attack_bonus = 3) 

class pitchfork(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=5, attack_bonus = 3) 

class pointy_stick(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=3, attack_bonus = 3) 

class wooden_spear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=3, attack_bonus = 4) 

class spike_on_a_stick(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 3) 

class simple_knife_spear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 4) 

class knife_spear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=5, attack_bonus = 4) 

class homemade_halfpike(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=5, attack_bonus = 2) 

class forked_spear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 2) 

class copper_spear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=5, attack_bonus = 3) 

class steel_spear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 4) 

class pipe_spear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=6, attack_bonus = 2) 

class sharpened_rebar(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 3) 

class qiang(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=6, attack_bonus = 2) 

class survivor_naginata(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=8, attack_bonus = 1) 

class wooden_javelin(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=2, attack_bonus = 6) 

class iron_javelin(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=5, attack_bonus = 2) 

class wooden_pike(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 0) 

class copper_pike(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=5, attack_bonus = 0) 

class pike(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=6, attack_bonus = 0) 

class dory(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=6, attack_bonus = 1) 

class ji(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=9, attack_bonus = 1) 

class crude_sword(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=5, attack_bonus = 4) 

class hand-forged_sword(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 2) 

class hunting_knife(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 5) 

class makeshift_machete(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = 4) 

class machete(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=6, attack_bonus = 5) 

class cavalry_saber(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 4) 

class kukri(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 4) 

class jian(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=8, attack_bonus = 6) 

class scimitar(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 4) 

class longsword(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=8, attack_bonus = 3) 

class arming_sword(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=9, attack_bonus = 4) 

class xiphos(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 5) 

class khopesh(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=5, attack_bonus = 4) 

class dao(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 3) 

class survivor_machete(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=6, attack_bonus = 5) 

class sword_bayonet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 4) 

class wakizashi(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=6, attack_bonus = 4) 

class zweihaender(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=8, attack_bonus = 1) 

class nodachi(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=8, attack_bonus = 1) 

class broadsword(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=8, attack_bonus = 5) 

class katana(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=8, attack_bonus = 4) 

class pair_of_butterfly_swords(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 3) 

class chainsaw_lajatang_(off)(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=1, attack_bonus = -19) 

class electric_chainsaw_lajatang_(off)(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=1, attack_bonus = -19) 

class cutlass(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=7, attack_bonus = 5) 

class lajatang(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=4, attack_bonus = -4) 

class combat_chainsaw_(off)(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=1, attack_bonus = -3) 

class electric_combat_chainsaw_(off)(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Weapon, power_bonus=1, attack_bonus = -3) 

class pair_of_2-by-arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=3, armor_bonus = 5)

class pair_of_chitin_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_hard_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_leather_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=3, armor_bonus = 6)

class pair_of_steel_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_metal_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=4, armor_bonus = 6)

class pair_of_paper_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_scrap_arm_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_neoprene_arm_sleeves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_chainmail_sleeves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_elbow_pads(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_leather_vambraces(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 4)

class pair_of_cord_sandals(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_chitinous_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_biosilicified_chitin_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_survivor_fireboots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_fur_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_survivor_wetsuit_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_heavy_survivor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=7, armor_bonus = 7)

class pair_of_leather_armor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=3, armor_bonus = 6)

class pair_of_light_survivor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_armored_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class pair_of_scrap_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_survivor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class pair_of_winter_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class pair_of_winter_survivor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class pair_of_XL_survivor_boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class pair_of_wooden_clogs(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=4, armor_bonus = 6)

class pair_of_foot_rags(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_fur_foot_wraps(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_leather_foot_wraps(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_wool_foot_wraps(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_geta(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_leather_sandals(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 3)

class pair_of_moccasins(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_birchbark_shoes(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_straw_sandals(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 3)

class pair_of_swim_fins(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_swimming_booties(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 5)

class pair_of_chainmail_chausses(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_flame-resistant_socks(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_socks(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 5)

class pair_of_ankle_socks(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_bag_socks(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_wool_socks(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 5)

class pair_of_stockings(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_tabi(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 5)

class pair_of_chainmail_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_chitinous_gauntlets(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_biosilicified_chitin_gauntlets(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_leather_armor_gauntlets(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=3, armor_bonus = 5)

class pair_of_bag_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_fingerless_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_armored_fingerless_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_survivor_firegloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_fur_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class pair_of_heavy_survivor_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=4, armor_bonus = 6)

class pair_of_leather_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_light_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_glove_liners(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_light_survivor_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_fingerless_survivor_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_armored_gauntlets(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class pair_of_survivor_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_wool_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_work_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_hand_wraps(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_fur_hand_wraps(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_leather_hand_wraps(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_wool_hand_wraps(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class pair_of_winter_survivor_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class pair_of_XL_survivor_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_mittens(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class pair_of_flame-resistant_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_sock_mitts(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 3)

class pot_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class barbute_helm(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class chitinous_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class conical_helm(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class biosilicified_chitin_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class galea(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class kabuto(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class leather_armor_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=3, armor_bonus = 5)

class nasal_helm(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class nomad_cowl(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class great_helm(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class scavenger_cowl(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class scrap_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class survivor_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class XL_survivor_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class heavy_survivor_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=7, armor_bonus = 7)

class Corinthian_helm(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=5, armor_bonus = 6)

class XL_pot_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=4, armor_bonus = 5)

class pair_of_2-by-shin_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=3, armor_bonus = 5)

class chainmail_leggings(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class leather_chaps(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class pair_of_knee_pads(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 4)

class pair_of_bronze_greaves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_hard_leg_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_steel_leg_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_iron_greaves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_paper_leg_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class pair_of_scrap_leg_guards(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class light_survivor_cargo_pants(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class survivor_cargo_pants(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class AEP_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=3, armor_bonus = 6)

class ANBC_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=3, armor_bonus = 6)

class boiled_leather_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=4, armor_bonus = 6)

class chitinous_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class biosilicified_chitin_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=0, armor_bonus = 4)

class fur_body_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=3, armor_bonus = 6)

class leather_body_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=3, armor_bonus = 6)

class plate_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class nomad_gear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class light_nomad_gear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class plated_leather_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=3, armor_bonus = 6)

class ornamental_plate_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class O-yoroi(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class scavenger_gear(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class scrap_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class chainmail_hauberk(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class chainmail_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class faraday_chainmail_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class entry_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class survivor_firesuit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class gambeson(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class heavy_survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class light_survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class flame-resistant_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class winter_survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class XL_survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class XL_heavy_survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class bell_cuirass(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=5, armor_bonus = 6)

class lamellar_cuirass(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class lorica_segmentata(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class bookplate(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=4, armor_bonus = 6)

class chainmail_vest(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class cuirass(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class scrap_cuirass(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class armored_leather_jacket(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

class light_survivor_body_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=1, armor_bonus = 5)

class armored_leather_vest(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.Armor, defense_bonus=2, armor_bonus = 5)

