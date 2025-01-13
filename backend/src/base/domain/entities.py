from pydantic import BaseModel, Field
from datetime import date, time
from ..types import IngredientType, UnitType


class NamedEntity(BaseModel):
    name: str


class DateTimeObject(BaseModel):
    date: date
    time: time


class Quantifiable(BaseModel):
    quantity: float
    unit: UnitType


class Item(NamedEntity):
    code: int
    leadtime: float


class ItemStock(Quantifiable):
    item: Item


class Mixer(Entity, Quantifiable):
    speed: float
    changeover_time: float





class PurchasingPlan(DateTimeObject, Quantifiable):
    item: Item
    supplier: str


class ShipmentPlan(DateTimeObject, Quantifiable):
    item: Item
    client: str


class ProcurementPlan(DateTimeObject, Quantifiable):
    item: Item
    working_hours: float
