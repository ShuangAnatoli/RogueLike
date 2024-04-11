import json
import pandas as pd
import numpy as np
import math
import string
import pathlib

targets_armor_list = [["arms_armor", "arms"], ["boots", "feet"], ["gloves", "hands"], ["helmets", "head"], ["legs_armor", "legs"], ["shields", "other"], ["suits_protection", "suit"], ["torso_armor", "torso"]]
targets_ranged_list = ["archery", "crossbow", "slings", "throwing"]
targets_melee_list = [["bludgeons", "bashing"], ["spears_and_polearms", "piercing"], ["swords_and_blades", "cutting"]]

#Path: Find in data/json/items. Then search data/json/recipes/[armor, weapon, or ammo]
#TODO: manually make ammo categories? Steal from simple guns mod?
#TODO: check each category for unecessary stuff, remove

stat_path = "C:/Users/r2d2go/Downloads/BN---Primitive-Launcher-0.9.6/data/json/items"
recipe_path = "C:/Users/r2d2go/Downloads/BN---Primitive-Launcher-0.9.6/data/json/recipes"
material_path = "C:/Users/r2d2go/Downloads/BN---Primitive-Launcher-0.9.6/data/json/materials.json"
ranged_path = "C:/Users/r2d2go/Downloads/BN---Primitive-Launcher-0.9.6/data/json/recipes/weapon/ranged.json"

material_df = pd.read_json(material_path)

big_armor_df = pd.DataFrame({'item_name' : []})
# big_armor_df["recipe"] = ""
# big_armor_df["craft_level"] = ""
# big_armor_df["protection"] = ""
# big_armor_df["armor"] = ""
# big_armor_df["mitigation"] = ""
# big_armor_df["acid_res"] = ""
# big_armor_df["elec_res"] = ""
# big_armor_df["fire_res"] = ""
# big_armor_df["cold_res"] = ""

for armor in targets_armor_list:
    armor_item_df = pd.read_json(stat_path+f"/armor/{armor[0]}.json")
    armor_item_df["recipe"] = ""
    armor_item_df["craft_level"] = ""
    armor_item_df["protection"] = "0"
    armor_item_df["armor"] = "0"
    armor_item_df["mitigation"] = "0"
    armor_item_df["acid_res"] = ""
    armor_item_df["elec_res"] = ""
    armor_item_df["fire_res"] = ""
    armor_item_df["cold_res"] = ""
    armor_recipe_df = pd.read_json(recipe_path+f"/armor/{armor[1]}.json")
    
    
    for index, row in armor_item_df.iterrows():
        try:
            armor_recipe_index = armor_recipe_df[armor_recipe_df["result"] == row["id"]].index[0]
        except:
            pass
        else:
            armor_item_df.at[index,"recipe"] = armor_recipe_df.at[armor_recipe_index, "components"]
            armor_item_df.at[index,"craft_level"] = armor_recipe_df.at[armor_recipe_index, "difficulty"]
            armor_mats = armor_item_df.at[index,"material"]
            
            thickness = armor_item_df.at[index,"material_thickness"]
            try: 
                round(thickness)
            except:
                thickness = 1
            coverage = armor_item_df.at[index,"coverage"]
            try:
                round(coverage)
            except:
                coverage = 50
            bash_res = 0
            cut_res = 0
            acid_res = 0
            elec_res = 0
            fire_res = 0
            armor_item_df.at[index, "cold_res"] = armor_item_df.at[index,"warmth"]/5

            
            for mat in armor_mats:
                row = material_df.loc[material_df['id'] == mat]
                bash_res = int(row["bash_resist"].iloc[0])
                cut_res = int(row["cut_resist"].iloc[0])
                acid_res = int(row["acid_resist"].iloc[0])
                elec_res = int(row["elec_resist"].iloc[0])
                fire_res = int(row["fire_resist"].iloc[0])
            num_mats = len(armor_mats)
            bash_res /= num_mats/thickness
            
            cut_res /= num_mats/thickness
            try:
                round(bash_res)
            except:
                bash_res = 0
            try:
                round(cut_res)
            except:
                cut_res = 0
            armor_item_df.at[index,"elec_res"] = round(elec_res/num_mats*thickness)
            armor_item_df.at[index,"fire_res"] = round(fire_res/num_mats*thickness)
            armor_item_df.at[index,"acid_res"] = round(acid_res/num_mats*thickness)
            #PROTECTION (reduce dismemberment)
            protection_val = (2*cut_res+bash_res)*coverage/16
            sigmoid_two_prot = 1/(1+2**(-protection_val/8)) #between 50% and 100%, positive sigmoid
            protection_final = sigmoid_two_prot*(coverage/128+(1-1/1.28))
            #another coverage multiplier; 0% -> 22%, 50% -> 61%, 100% -> 100%, linear
            armor_item_df.at[index,"protection"] = protection_final #percentage reduction of dismemberment chance to this body part.

            #MITIGATION (flat damage reduction)
            mitigation_final = round((156+coverage)/256*(cut_res+2*bash_res)/4)

            
            try:
                protection_final > 0
            except:
                protection_final = 0

                
            try:
                float(mitigation_final) > 0
            except:
                mitigation_final = 0

            armor_final = round((2*protection_final-0.5)*(20+mitigation_final)*3/16)
            
            
            
            #above, 156+coverage/256 gives flattened coverage multiplier, /8 with x1.5 from the 2+1 gives 5.33, to approx match 32/(64+speed). Should be 5-20 range
            armor_item_df.at[index,"mitigation"] = mitigation_final #flat damage reduction
        
            #ARMOR (avoid getting hit, as D&D)
            armor_item_df.at[index,"armor"] = armor_final
            try: 
                armor_item_df.at[index,"craft_level"] > 0
            except:
                armor_item_df.at[index,"craft_level"] = round((mitigation_final+armor_final)/5)



    big_armor_df = big_armor_df._append(armor_item_df[["name", "armor", "mitigation", "recipe", "craft_level", "elec_res", "fire_res", "acid_res", "cold_res", "protection"]].fillna(0))

        
big_melee_df = pd.DataFrame({'item_name' : []})
big_melee_df["recipe"] = ""
big_melee_df["craft_level"] = ""
big_melee_df["attack"] = "0"
big_melee_df["type"] = ""
big_melee_df["power"] = "0"
big_melee_df["init"] = ""


for melee in targets_melee_list:
    melee_item_df = pd.read_json(stat_path+f"/melee/{melee[0]}.json")
    melee_item_df["recipe"] = ""
    melee_item_df["craft_level"] = ""
    melee_item_df["attack"] = "0"
    melee_item_df["type"] = ""
    melee_item_df["power"] = "0"
    melee_item_df["init"] = ""
    melee_recipe_df = pd.read_json(recipe_path+f"/weapon/{melee[1]}.json")
    
    melee_item_df = melee_item_df.dropna(subset=["weight", "volume"])
    for index, row in melee_item_df.iterrows():
        try:
            melee_recipe_index = melee_recipe_df[melee_recipe_df["result"] == row["id"]].index[0]
        except:
            pass
        else:
            melee_item_df.at[index,"recipe"] = melee_recipe_df.at[melee_recipe_index, "components"]

            try:
                len(melee_recipe_df.at[index,"using"])
            except:
                pass
            else:
                for i in range(len(melee_recipe_df.at[index,"using"])):
                    if melee_recipe_df.at[index,"using"][i][0] == "steel_standard":
                        num_steel = melee_recipe_df.at[index,"using"][i][1]*3
                        melee_item_df.at[index,"recipe"].append([["steel", num_steel]])
                    elif melee_recipe_df.at[index,"using"][i][0] == "steel_tiny":
                        num_steel = melee_recipe_df.at[index,"using"][i][1]
                        melee_item_df.at[index,"recipe"].append([["steel", num_steel]])
                        
                    elif melee_recipe_df.at[index,"using"][i][0] == "bronzesmithing_tools":
                        num_bronze = melee_recipe_df.at[index,"using"][i][1]
                        melee_item_df.at[index,"recipe"].append([["scrap_bronze", num_bronze]])
            
            melee_item_df.at[index,"craft_level"] = melee_recipe_df.at[melee_recipe_index, "difficulty"]
            bash = melee_item_df.at[index,"bashing"]
            try:
                round(bash)
            except:
                bash = 0
            cut = melee_item_df.at[index,"cutting"]
            try:
                round(cut)
            except:
                cut = 0
            if bash > cut:
                melee_item_df.at[index,"type"] = "BASH"
            else:
                melee_item_df.at[index,"type"] = "CUT"
            try:
                if "STAB" in melee_item_df.at[index,"flags"]:
                    melee_item_df.at[index,"type"] = "STAB"
            except:
                pass
            total_damage = bash+cut
            weight = melee_item_df.at[index,"weight"][:-2] #cuts off g
            volume = melee_item_df.at[index,"volume"][:-3] #cuts off ml

            try:
                weight = float(weight)
            except:
                weight = 1000
            try:
                volume = float(volume)
            except:
                volume = 1000

            swing_time = 64+weight/64+volume/64 #CDDA's formula but tweaked; 250/4 -> 64, 60 -> 64

            melee_item_df.at[index,"init"] = round(100-swing_time)/8
            to_hit = melee_item_df.at[index, "to_hit"]
            if pd.isna(melee_item_df.at[index, "to_hit"]):
                to_hit = 0
            melee_item_df.at[index, "attack"] = to_hit+round((150-swing_time)/16)
            final_dmg_avg = round(total_damage/(65+swing_time)*32)

            melee_item_df.at[index, "power"] = final_dmg_avg

            
            try: 
                melee_item_df.at[index,"craft_level"] >= 0
            except:
                melee_item_df.at[index,"craft_level"] = round((final_dmg_avg+to_hit*4)/8)
            #TODO: base damage on bash/stab/cut
            #Dismemberment has different forms: broken/bleeding/removed
    big_melee_df = big_melee_df._append(melee_item_df[["name", "attack", "power", "recipe", "craft_level"]]).fillna(0)


# big_ranged_df = pd.DataFrame({'item_name' : []})
# big_ranged_df["recipe"] = ""
# big_ranged_df["craft_level"] = ""
# big_ranged_df["attack"] = ""
# big_ranged_df["type"] = ""
# big_ranged_df["power"] = ""
# big_ranged_df["init"] = 0

# for ranged in targets_ranged_list:
#     ranged_item_df = pd.read_json(stat_path+f"/ranged/{ranged[0]}.json")
#     ranged_item_df["recipe"] = ""
#     ranged_item_df["craft_level"] = ""
#     ranged_item_df["attack"] = ""
#     ranged_item_df["type"] = ""
#     ranged_item_df["power"] = ""
#     ranged_item_df["init"] = 0
#     ranged_recipe_df = pd.read_json(recipe_path+f"/weapon/ranged.json")
#     for index, row in ranged_item_df.iterrows():
#         ranged_item_df.at[index,"recipe"] = ranged_recipe_df.at[row["id"],"components"]
#         ranged_item_df.at[index,"craft_level"] = ranged_recipe_df.at[row["id"],"difficulty"]
#         total_damage = ranged_item_df.at[index,"ranged_damage"]["amount"]
#         type = ranged_item_df.at[index,"ranged_damage"]["damage type"]
#         ranged_item_df.at[index,"type"] = string.upper(type)
#         weight = ranged_item_df.at[index,"weight"][:-2] #cuts off g
#         volume = ranged_item_df.at[index,"volume"][:-3] #cuts off ml
#         swing_time = 64+weight/64+volume/64 #CDDA's formula but tweaked; 250/4 -> 64, 60 -> 64
#         init = 4-round(swing_time/32)
#         final_dmg_avg = round(total_damage/2)
#         ranged_item_df[index, "attack"] = ranged_item_df[index, "to_hit"]
#         ranged_item_df["power"] = final_dmg_avg

#     big_ranged_df = big_ranged_df.append(ranged_item_df)
 

big_melee_df = big_melee_df[(big_melee_df['power'].ne("0") & big_melee_df['attack'].ne("0"))]
filepath = pathlib.Path('data/melee.json') 
big_melee_df.reset_index(inplace=True)
filepath.parent.mkdir(parents=True, exist_ok=True)  
big_melee_df.to_json(filepath, orient="index", lines=True)


big_armor_df = big_armor_df[(big_armor_df['mitigation'].ne("0") & big_armor_df['armor'].ne("0"))]
filepath = pathlib.Path('data/armor.json') 
big_armor_df.reset_index(inplace=True)
filepath.parent.mkdir(parents=True, exist_ok=True)  
big_armor_df.to_json(filepath, orient="records", lines=True)

with open("final_path.txt", "w") as f:
    for index, melee_item in big_melee_df.iterrows():
        try:
            f.write(f"class {melee_item['name']['str'].replace(' ', '_')}(Equippable): \n")
        except:
            f.write(f"class {melee_item['name']['str_sp'].replace(' ', '_')}(Equippable): \n")
        f.write(f"\tdef __init__(self) -> None:\n")
        # f.write(f"""\t\tsuper().__init__(equipment_type=EquipmentType.Weapon, 
        #         power_bonus={int(melee_item['power'])}, 
        #         attack_bonus = {int(melee_item['attack'])},
        #         craft_level = {int(melee_item['craft_level'])},
        #         recipe = [{', '.join(f"[{item[0][0]}, {str(item[0][1])}]" for item in melee_item['recipe'])})]
        #         \n\n""")
    # for ranged_item in big_ranged_df.iterrows():
    #     f.write(f"class {ranged_item['name']['str']}Equippable \n")
    #     f.write(f"\tdef __init__(self) -> None:\n")
    #     f.write(f"\tsuper().__init__(equipment_type=EquipmentType.Weapon), power_bonus={ranged_item['power']}, attack_bonus = {ranged_item['attack']}")
        

    for index, armor_item in big_armor_df.iterrows():
        try:
            f.write(f"class {armor_item['name']['str'].replace(' ', '_')}(Equippable): \n")
        except:
            f.write(f"class {armor_item['name']['str_sp'].replace(' ', '_')}(Equippable): \n")
        f.write(f"\tdef __init__(self) -> None:\n")
        f.write(f"""\t\tsuper().__init__(equipment_type=EquipmentType.Armor, 
                defense_bonus = {int(armor_item['mitigation'])}, 
                armor_bonus = {int(armor_item['armor'])},
                craft_level = {int(armor_item['craft_level'])},
                recipe = [{', '.join(f"{item}"[1:-1] for item in armor_item['recipe'])}])\n\n""")

#TODO: Material conversions. e.g. Log -> long stick takes X hours.
                
# class Sword(Equippable):
#     def __init__(self) -> None:
#         super().__init__(equipment_type=EquipmentType.WEAPON, power_bonus=4)

