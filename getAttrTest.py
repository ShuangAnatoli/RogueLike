from importlib import import_module
import importlib.util
from components import equippable
class_ = getattr(equippable, "Sword")
instance = class_()