from pydantic import BaseModel
from .base import BaseEntity, BaseQuantifiable
from ...types.unit import UnitType


class Item(BaseEntity):
    code: int
    name: str
    leadtime: float


class ItemStock(BaseQuantifiable):
    item: Item
