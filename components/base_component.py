from __future__ import annotations

import sys

sys.path.append('../tcod_tutorial_v2')
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from tcod_tutorial_v2.engine import Engine
    from tcod_tutorial_v2.entity import Entity
    from tcod_tutorial_v2.game_map import GameMap


class BaseComponent:
    parent: Entity  # Owning entity instance.

    @property
    def gamemap(self) -> GameMap:
        return self.parent.gamemap

    @property
    def engine(self) -> Engine:
        return self.gamemap.engine
