from .entities import (
    Item,
    Mixer,
    Recipe,
)

from pydantic import BaseModel


class Master(BaseModel):
    items: list[Item]
    mixers: list[Mixer]
    recipes: list[Recipe]
