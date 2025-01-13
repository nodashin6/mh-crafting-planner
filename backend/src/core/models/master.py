from ..domain.entities import (
    Item,
    Mixer,
    Recipe,
)

from pydantic import BaseModel


class CraftingMaster(BaseModel):
    items: list[Item]
    mixers: list[Mixer]
    recipes: list[Recipe]
