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
		armor_bonus: int = 0,
		recipe = ["unobtanium"],
		craft_level = 5
	):
		self.equipment_type = equipment_type

		self.power_bonus = power_bonus
		self.attack_bonus = attack_bonus
		self.armor_bonus = armor_bonus
		self.defense_bonus = defense_bonus
		self.craft_level = craft_level

		self.recipe = recipe


class Dagger(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=2)


class Sword(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=4)


class LeatherArmor(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=1)


class ChainMail(Equippable):
    def __init__(self) -> None:
        super().__init__(equipment_type=EquipmentType.ARMOR, defense_bonus=3)

class armguard_chitin(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMS, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 4,
                recipe = [['string_36', 1], ['string_6', 4], ['chitin_piece', 4], ['leather', 4]])

class armguard_hard(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMS, 
                defense_bonus = 2, 
                armor_bonus = 4,
                craft_level = 4,
                recipe = [['neoprene', 6], ['plastic_chunk', 8]])

class armguard_larmor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMS, 
                defense_bonus = 6, 
                armor_bonus = 7,
                craft_level = 3,
                recipe = [['leather', 12], ['fur', 12]])

class armguard_lightplate(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMS, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 7,
                recipe = [['steel_lump', 6], ['steel_chunk', 24], ['fur', 6], ['leather', 6]])

class armguard_metal(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMS, 
                defense_bonus = 8, 
                armor_bonus = 6,
                craft_level = 4,
                recipe = [['sheet_metal_small', 4]])

class armguard_paper(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMS, 
                defense_bonus = 2, 
                armor_bonus = 5,
                craft_level = 0,
                recipe = [['paper', 60], ['duct_tape', 10]])

class armguard_scrap(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMS, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 3,
                recipe = [['scrap', 60]])

class armguard_soft(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMS, 
                defense_bonus = 1, 
                armor_bonus = 3,
                craft_level = 3,
                recipe = [['neoprene', 4], ['rag', 2]])

class chainmail_arms(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMS, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 7,
                recipe = [['link_sheet', 3], ['chain_link', 75], ['wire', 1], ['fur', 6], ['leather', 6]])

class elbow_pads(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMS, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 4,
                recipe = [['plastic_chunk', 4], ['rag', 2], ['leather', 2], ['fur', 2]])

class vambrace_larmor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMS, 
                defense_bonus = 4, 
                armor_bonus = 3,
                craft_level = 2,
                recipe = [['leather', 4], ['fur', 4]])

class bastsandals(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 2,
                recipe = [['filament', 140, 'LIST']])

class boots(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 2,
                recipe = [['leather', 10]])

class boots_chitin(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 4,
                recipe = [['chitin_piece', 16], ['leather', 16]])

class boots_acidchitin(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 5,
                recipe = [['acidchitin_piece', 16], ['leather', 16]])

class boots_fsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 8,
                recipe = [['nomex', 8], ['kevlar_plate', 4], ['duct_tape', 200], ['nomex_socks', 1], ['boots_combat', 1], ['boots_steel', 1], ['boots_bunker', 1]])

class boots_fur(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 2, 
                armor_bonus = 5,
                craft_level = 2,
                recipe = [['leather', 7], ['fur', 7]])

class boots_h20survivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 7,
                recipe = [['plastic_chunk', 4], ['kevlar_plate', 4], ['duct_tape', 200], ['wetsuit_booties', 1], ['boots_combat', 1], ['boots_steel', 1], ['boots_bunker', 1]])

class boots_hsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 14, 
                armor_bonus = 10,
                craft_level = 7,
                recipe = [['rag', 4], ['leather', 4], ['steel_chunk', 4], ['scrap', 12], ['kevlar_plate', 4], ['duct_tape', 100], ['boots_combat', 1], ['boots_steel', 1], ['boots_hiking', 1], ['boots_bunker', 1], ['boots', 1]])

class boots_larmor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 6, 
                armor_bonus = 7,
                craft_level = 2,
                recipe = [['leather', 18], ['fur', 18]])

class boots_lsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 5,
                recipe = [['rag', 8], ['kevlar_plate', 4], ['duct_tape', 100], ['boots_combat', 1], ['boots_steel', 1], ['boots_hiking', 1], ['boots_bunker', 1], ['boots', 1]])

class boots_plate(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 5,
                recipe = [['fur', 16], ['leather', 16]])

class boots_scrap(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 3,
                recipe = [['scrap', 50]])

class boots_survivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 4, 
                armor_bonus = 7,
                craft_level = 6,
                recipe = [['leather', 8], ['kevlar_plate', 4], ['duct_tape', 100], ['boots_combat', 1], ['boots_steel', 1], ['boots_hiking', 1], ['boots_bunker', 1], ['boots', 1]])

class boots_winter(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 4, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['felt_patch', 20], ['bag_plastic', 8]])

class boots_wsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 4, 
                armor_bonus = 7,
                craft_level = 7,
                recipe = [['fur', 12], ['kevlar_plate', 4], ['duct_tape', 100], ['boots_combat', 1], ['boots_steel', 1], ['boots_hiking', 1], ['boots_bunker', 1], ['boots', 1]])

class boots_xlsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['leather', 24], ['rag', 6], ['scrap', 4], ['boots_combat', 2], ['kevlar_plate', 10], ['duct_tape', 200]])

class clogs(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 8, 
                armor_bonus = 7,
                craft_level = 3,
                recipe = [['2x4', 2], ['stick', 2]])

class footrags(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 2,
                craft_level = 0,
                recipe = [['rag', 6]])

class footrags_fur(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 3,
                craft_level = 0,
                recipe = [['fur', 9], ['cured_pelt', 9]])

class footrags_leather(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 3,
                craft_level = 0,
                recipe = [['leather', 9], ['cured_hide', 9]])

class footrags_wool(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 2,
                craft_level = 0,
                recipe = [['felt_patch', 6]])

class geta(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 1,
                recipe = [['2x4', 1], ['cordage_short', 1, 'LIST']])

class leathersandals(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 0,
                craft_level = 1,
                recipe = [['leather', 3]])

class mocassins(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 2,
                craft_level = 1,
                recipe = [['fur', 2]])

class shoes_birchbark(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 2, 
                armor_bonus = 2,
                craft_level = 2,
                recipe = [['birchbark', 3]])

class straw_sandals(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 1,
                recipe = [['straw_pile', 4], ['birchbark', 6]])

class swim_fins(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 4,
                recipe = [['plastic_chunk', 8], ['duct_tape', 80], ['medical_tape', 80], ['superglue', 1]])

class wetsuit_booties(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 4,
                recipe = [['neoprene', 2], ['rag', 2]])

class chainmail_feet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 7,
                recipe = [['link_sheet', 2], ['chain_link', 50], ['wire', 1], ['rag', 4]])

class nomex_socks(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['nomex', 9]])

class socks(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 0,
                recipe = [['rag', 2]])

class socks_ankle(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 3,
                craft_level = 0,
                recipe = [['rag', 2]])

class socks_bag(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 3,
                craft_level = 0,
                recipe = [['plastic_shopping_bag', 2]])

class socks_wool(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 1,
                recipe = [['yarn', 75]])

class stockings(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 3,
                craft_level = 1,
                recipe = [['rag', 8]])

class tabi_dress(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.FEET, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 1,
                recipe = [['rag', 3]])

class chainmail_hands(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 7,
                recipe = [['link_sheet', 2], ['chain_link', 50], ['wire', 1], ['rag', 4]])

class gauntlets_chitin(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 4,
                recipe = [['cordage_superior', 1, 'LIST'], ['chitin_piece', 3], ['leather', 3]])

class gauntlets_acidchitin(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 5,
                recipe = [['cordage_superior', 1, 'LIST'], ['acidchitin_piece', 3], ['leather', 3]])

class gauntlets_larmor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 5, 
                armor_bonus = 4,
                craft_level = 2,
                recipe = [['leather', 6], ['fur', 6]])

class gloves_bag(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 3,
                craft_level = 0,
                recipe = [['plastic_shopping_bag', 2]])

class gloves_fingerless(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 2,
                craft_level = 0,
                recipe = [['gloves_leather', 1]])

class gloves_fingerless_mod(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 1,
                recipe = [['gloves_fingerless', 1], ['scrap', 2]])

class gloves_fsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 8,
                recipe = [['nomex', 6], ['leather', 2], ['duct_tape', 120], ['gloves_tactical', 1], ['kevlar_plate', 4], ['nomex_gloves', 1], ['fire_gauntlets', 1]])

class gloves_fur(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 4, 
                armor_bonus = 6,
                craft_level = 2,
                recipe = [['fur', 4]])

class gloves_hsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 9, 
                armor_bonus = 8,
                craft_level = 7,
                recipe = [['rag', 2], ['leather', 2], ['scrap', 4], ['duct_tape', 50], ['gloves_tactical', 1], ['kevlar_plate', 4], ['gloves_leather', 1], ['gloves_light', 1], ['gloves_liner', 1], ['wetsuit_gloves', 1], ['fire_gauntlets', 1]])

class gloves_leather(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 2,
                recipe = [['leather', 2]])

class gloves_light(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 1,
                recipe = [['rag', 4]])

class gloves_liner(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 4,
                craft_level = 1,
                recipe = [['rag', 2]])

class gloves_lsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 5,
                recipe = [['rag', 6], ['leather', 2], ['duct_tape', 80], ['gloves_tactical', 1], ['kevlar_plate', 4], ['gloves_leather', 1], ['gloves_light', 1], ['gloves_liner', 1], ['wetsuit_gloves', 1], ['fire_gauntlets', 1]])

class gloves_survivor_fingerless(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 4,
                craft_level = 0,
                recipe = [['gloves_lsurvivor', 1]])

class gloves_plate(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['fur', 10], ['leather', 10]])

class gloves_survivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['rag', 2], ['leather', 6], ['duct_tape', 80], ['gloves_tactical', 1], ['kevlar_plate', 4], ['gloves_leather', 1], ['gloves_light', 1], ['gloves_liner', 1], ['wetsuit_gloves', 1], ['fire_gauntlets', 1]])

class gloves_wool(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 1,
                recipe = [['felt_patch', 4]])

class gloves_work(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 2,
                recipe = [['leather', 2], ['gloves_leather', 1], ['rag', 2], ['gloves_light', 1]])

class gloves_wraps(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 0,
                recipe = [['rag', 4]])

class gloves_wraps_fur(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 2,
                craft_level = 0,
                recipe = [['fur', 6], ['cured_pelt', 6]])

class gloves_wraps_leather(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 2,
                craft_level = 0,
                recipe = [['leather', 6], ['cured_hide', 6]])

class gloves_wraps_wool(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 0,
                recipe = [['felt_patch', 4]])

class gloves_wsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 7,
                recipe = [['rag', 2], ['fur', 8], ['duct_tape', 80], ['gloves_tactical', 1], ['kevlar_plate', 4], ['gloves_leather', 1], ['gloves_light', 1], ['gloves_liner', 1], ['wetsuit_gloves', 1], ['fire_gauntlets', 1]])

class gloves_xlsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['leather', 16], ['rag', 6], ['scrap', 2], ['duct_tape', 160], ['gloves_tactical', 2], ['kevlar_plate', 6]])

class mittens(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 1,
                recipe = [['yarn', 250]])

class nomex_gloves(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['nomex', 6]])

class sockmitts(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HANDS, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 0,
                recipe = [['socks', 1]])

class pot_helmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 5, 
                armor_bonus = 4,
                craft_level = 0,
                recipe = [['rag', 4], ['pot', 1]])

class helmet_barbute(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['fur', 4], ['leather', 4]])

class helmet_chitin(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 4,
                recipe = [['cordage_superior', 1, 'LIST'], ['chitin_piece', 6], ['leather', 6]])

class helmet_conical(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 2, 
                armor_bonus = 5,
                craft_level = 6,
                recipe = [['fur', 6]])

class helmet_acidchitin(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 5,
                recipe = [['cordage_superior', 1, 'LIST'], ['acidchitin_piece', 6], ['leather', 6]])

class helmet_galea(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 7,
                recipe = [['fur', 4], ['leather', 4]])

class helmet_kabuto(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 9,
                recipe = [['fur', 14], ['leather', 14], ['rag', 4]])

class helmet_larmor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 6, 
                armor_bonus = 6,
                craft_level = 4,
                recipe = [['leather', 16], ['fur', 16]])

class helmet_nasal(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 5,
                recipe = [['fur', 3], ['leather', 3]])

class helmet_nomad(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 5,
                recipe = [['hat_ball', 1], ['hat_boonie', 1], ['glasses_safety', 1], ['glasses_bal', 1], ['leather', 8]])

class helmet_plate(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 4, 
                armor_bonus = 7,
                craft_level = 7,
                recipe = [['fur', 4], ['leather', 4]])

class helmet_scavenger(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 8,
                recipe = [['hat_ball', 1], ['hat_boonie', 1], ['mask_filter', 1], ['glasses_bal', 1], ['goggles_ski', 1], ['kevlar_plate', 8]])

class helmet_scrap(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 3,
                recipe = [['scrap', 30]])

class helmet_survivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 4, 
                armor_bonus = 7,
                craft_level = 6,
                recipe = [['helmet_liner', 1], ['hat_cotton', 1], ['rag', 3], ['tac_helmet', 1], ['tac_fullhelmet', 1], ['helmet_army', 1], ['kevlar_plate', 6], ['hood_rain', 1], ['bag_plastic', 2], ['leather', 8], ['duct_tape', 150], ['helmet_riot', 1], ['helmet_motor', 1], ['helmet_football', 1], ['helmet_ball', 1], ['helmet_skid', 1], ['helmet_bike', 1], ['hat_hard', 1], ['firehelmet', 1], ['pickelhaube', 1], ['plastic_chunk', 8]])

class helmet_xlsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['scrap', 4], ['rag', 6], ['leather', 16], ['plastic_chunk', 20], ['kevlar_plate', 14], ['hood_rain', 2], ['bag_plastic', 4], ['duct_tape', 300]])

class helmet_hsurvivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 14, 
                armor_bonus = 10,
                craft_level = 7,
                recipe = [['helmet_liner', 1], ['hat_cotton', 1], ['rag', 3], ['helmet_army', 1], ['hood_rain', 1], ['bag_plastic', 2], ['steel_chunk', 2], ['scrap', 6], ['duct_tape', 75], ['helmet_riot', 1], ['helmet_motor', 1], ['helmet_football', 1], ['helmet_ball', 1], ['helmet_skid', 1], ['helmet_bike', 1], ['hat_hard', 1], ['firehelmet', 1], ['pickelhaube', 1], ['plastic_chunk', 8]])

class helmet_corinthian(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 9, 
                armor_bonus = 7,
                craft_level = 6,
                recipe = [['scrap_bronze', 7], ['fur', 4], ['leather', 4]])

class pot_xlhelmet(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.HEAD, 
                defense_bonus = 7, 
                armor_bonus = 4,
                craft_level = 0,
                recipe = [['rag', 10], ['pot_canning', 1]])

class chainmail_legs(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.LEGS, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 7,
                recipe = [['link_sheet', 4], ['chain_link', 100], ['wire', 1], ['rag', 6]])

class chaps_leather(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.LEGS, 
                defense_bonus = 4, 
                armor_bonus = 4,
                craft_level = 4,
                recipe = [['leather', 8]])

class knee_pads(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.LEGS, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 4,
                recipe = [['plastic_chunk', 8], ['rag', 4], ['leather', 4], ['fur', 4]])

class legguard_bronze(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.LEGS, 
                defense_bonus = 3, 
                armor_bonus = 4,
                craft_level = 5,
                recipe = [['fur', 6], ['leather', 6], ['scrap_bronze', 12]])

class legguard_hard(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.LEGS, 
                defense_bonus = 2, 
                armor_bonus = 4,
                craft_level = 3,
                recipe = [['neoprene', 6], ['plastic_chunk', 8]])

class legguard_lightplate(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.LEGS, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 7,
                recipe = [['fur', 6], ['leather', 6]])

class legguard_metal(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.LEGS, 
                defense_bonus = 3, 
                armor_bonus = 4,
                craft_level = 5,
                recipe = [['fur', 6], ['leather', 6]])

class legguard_paper(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.LEGS, 
                defense_bonus = 2, 
                armor_bonus = 5,
                craft_level = 0,
                recipe = [['paper', 60], ['duct_tape', 10]])

class legguard_scrap(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.LEGS, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 3,
                recipe = [['scrap', 60]])

class lsurvivor_pants(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.LEGS, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 5,
                recipe = [['rag', 15], ['bag_plastic', 4], ['legrig', 1], ['tool_belt', 1], ['ragpouch', 4], ['leather_pouch', 2], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 50], ['kevlar_plate', 8]])

class pants_survivor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.LEGS, 
                defense_bonus = 4, 
                armor_bonus = 7,
                craft_level = 6,
                recipe = [['pants_army', 1], ['pants_cargo', 1], ['shorts_cargo', 1], ['kevlar', 1], ['modularvest', 1], ['kevlar_plate', 12], ['rag', 12], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 4], ['leather_pouch', 2], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 100]])

class aep_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 5, 
                armor_bonus = 7,
                craft_level = 6,
                recipe = [['cleansuit', 1], ['duct_tape', 600], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24], ['plastic_sheet', 1]])

class anbc_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 5, 
                armor_bonus = 7,
                craft_level = 8,
                recipe = [['hazmat_suit', 1], ['duct_tape', 800], ['swat_armor', 1], ['kevlar_plate', 48], ['plastic_sheet', 1]])

class armor_blarmor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 7, 
                armor_bonus = 7,
                craft_level = 3,
                recipe = [['water', 10], ['water_clean', 10], ['wax', 2], ['any_tallow', 8, 'LIST'], ['vinegar', 10], ['pine_bough', 20], ['salt', 50], ['armor_larmor', 1], ['armguard_larmor', 1]])

class armor_chitin(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 4,
                recipe = [['chitin_piece', 36], ['leather', 36]])

class armor_acidchitin(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 1, 
                armor_bonus = 1,
                craft_level = 5,
                recipe = [['acidchitin_piece', 36], ['leather', 36]])

class armor_farmor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 6, 
                armor_bonus = 7,
                craft_level = 5,
                recipe = [['fur', 48]])

class armor_larmor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 6, 
                armor_bonus = 7,
                craft_level = 5,
                recipe = [['leather', 30], ['fur', 30]])

class armor_lightplate(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 8,
                recipe = [['fur', 20], ['leather', 20]])

class armor_nomad(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 4, 
                armor_bonus = 6,
                craft_level = 5,
                recipe = [['duster', 1], ['vest', 1], ['tacvest', 1], ['ragpouch', 1], ['leather_pouch', 1], ['dump_pouch', 1], ['fanny', 1], ['tool_belt', 1], ['legrig', 1], ['pants_cargo', 1], ['pants_army', 1], ['leather', 24]])

class armor_nomad_light(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 4,
                recipe = [['tunic', 1], ['shorts_cargo', 1], ['shorts_denim', 1], ['vest', 1], ['tacvest', 1], ['ragpouch', 2], ['dump_pouch', 2], ['fanny', 2], ['tool_belt', 1], ['legrig', 1], ['rag', 20]])

class armor_plarmor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 6, 
                armor_bonus = 7,
                craft_level = 2,
                recipe = [['steel_chunk', 6], ['scrap', 18], ['armor_larmor', 1], ['armguard_larmor', 1]])

class armor_plate(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 4, 
                armor_bonus = 6,
                craft_level = 9,
                recipe = [['fur', 16], ['leather', 16]])

class armor_samurai(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 9,
                recipe = [['fur', 28], ['leather', 28], ['rag', 10]])

class armor_scavenger(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 8,
                recipe = [['jacket_army', 1], ['vest', 1], ['tacvest', 1], ['mbag', 1], ['runner_bag', 1], ['fanny', 2], ['dump_pouch', 1], ['tool_belt', 1], ['legrig', 1], ['pants_army', 1], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class armor_scrapsuit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 3,
                recipe = [['scrap', 170]])

class chainmail_hauberk(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 2,
                recipe = [['chainmail_vest', 1], ['chainmail_arms', 1], ['chainmail_legs', 1], ['gambeson', 1]])

class chainmail_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 3,
                recipe = [['chainmail_hood', 1], ['chainmail_vest', 1], ['chainmail_arms', 1], ['chainmail_legs', 1], ['gambeson', 1]])

class chainmail_suit_faraday(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 7,
                recipe = [['link_sheet', 2], ['chainmail_hood', 1], ['link_sheet', 7], ['chainmail_vest', 1], ['link_sheet', 3], ['chainmail_arms', 1], ['link_sheet', 4], ['chainmail_legs', 1], ['link_sheet', 2], ['chainmail_hands', 1], ['link_sheet', 2], ['chainmail_feet', 1], ['chain_link', 500], ['wire', 5], ['rag', 26]])

class entry_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 5, 
                armor_bonus = 7,
                craft_level = 6,
                recipe = [['nomex', 40], ['kevlar_plate', 8], ['duct_tape', 200], ['superglue', 5], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class fsurvivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 8,
                recipe = [['rag', 4], ['nomex_suit', 1], ['entry_suit', 1], ['nomex', 20], ['coat_rain', 1], ['jacket_windbreaker', 1], ['jacket_evac', 1], ['coat_gut', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 200], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class gambeson(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 4, 
                armor_bonus = 6,
                craft_level = 4,
                recipe = [['rag', 26]])

class hsurvivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 7,
                recipe = [['rag', 20], ['leather', 20], ['steel_chunk', 4], ['scrap', 12], ['coat_rain', 1], ['jacket_windbreaker', 1], ['jacket_evac', 1], ['coat_gut', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 300], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class lsurvivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 5,
                recipe = [['rag', 30], ['coat_rain', 1], ['jacket_windbreaker', 1], ['jacket_evac', 1], ['coat_gut', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 200], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class nomex_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 2, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['nomex', 18]])

class survivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['rag', 20], ['leather', 20], ['coat_rain', 1], ['jacket_windbreaker', 1], ['jacket_evac', 1], ['coat_gut', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 300], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class wsurvivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 4, 
                armor_bonus = 7,
                craft_level = 6,
                recipe = [['rag', 10], ['leather', 20], ['fur', 20], ['coat_rain', 1], ['jacket_windbreaker', 1], ['jacket_evac', 1], ['coat_gut', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 300], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 24]])

class xlsurvivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 6,
                recipe = [['rag', 30], ['leather', 40], ['scrap', 8], ['coat_rain', 2], ['jacket_windbreaker', 2], ['jacket_evac', 2], ['coat_gut', 2], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 400], ['kevlar', 2], ['modularvest', 2], ['swat_armor', 2], ['kevlar_plate', 42]])

class xlhsurvivor_suit(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 8,
                recipe = [['rag', 30], ['leather', 40], ['steel_chunk', 8], ['scrap', 24], ['coat_rain', 2], ['jacket_windbreaker', 2], ['jacket_evac', 2], ['coat_gut', 2], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 6], ['leather_pouch', 4], ['dump_pouch', 1], ['purse', 2], ['fanny', 2], ['duct_tape', 400], ['kevlar', 2], ['modularvest', 2], ['swat_armor', 2], ['kevlar_plate', 48]])

class armor_cuirass(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 9, 
                armor_bonus = 7,
                craft_level = 5,
                recipe = [['scrap_bronze', 28]])

class armor_lamellar(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 3,
                recipe = [['cordage_superior', 4, 'LIST'], ['rag', 4], ['leather', 42], ['fur', 42]])

class armor_lorica(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 7,
                recipe = [['fur', 12], ['leather', 12]])

class bookplate(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 8, 
                armor_bonus = 6,
                craft_level = 3,
                recipe = [['paper', 1200], ['duct_tape', 150]])

class chainmail_vest(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 7,
                recipe = [['link_sheet', 7], ['chain_link', 175], ['wire', 1], ['rag', 6]])

class cuirass_lightplate(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 6,
                craft_level = 8,
                recipe = [['fur', 6], ['leather', 6]])

class cuirass_scrap(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 3, 
                armor_bonus = 5,
                craft_level = 3,
                recipe = [['scrap', 80]])

class jacket_leather_mod(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 4, 
                armor_bonus = 6,
                craft_level = 3,
                recipe = [['jacket_leather', 1], ['jacket_leather_red', 1], ['scrap', 9]])

class lsurvivor_armor(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 1, 
                armor_bonus = 5,
                craft_level = 5,
                recipe = [['rag', 15], ['coat_rain', 1], ['tacvest', 1], ['legrig', 1], ['vest', 1], ['tool_belt', 1], ['ragpouch', 2], ['leather_pouch', 2], ['dump_pouch', 1], ['purse', 1], ['fanny', 1], ['duct_tape', 150], ['kevlar', 1], ['modularvest', 1], ['swat_armor', 1], ['kevlar_plate', 16]])

class vest_leather_mod(Equippable): 
	def __init__(self) -> None:
		super().__init__(equipment_type=EquipmentType.ARMOR, 
                defense_bonus = 4, 
                armor_bonus = 6,
                craft_level = 3,
                recipe = [['vest_leather', 1], ['scrap', 5]])

