from pydantic import BaseModel, Field
from datetime import date, time
from ..types import IngredientType, UnitType


class Entity(BaseModel):
    code: int
    name: str


class DateTimeObject(BaseModel):
    code: int
    date: date
    time: time


class Quantifiable(BaseModel):
    quantity: float
    unit: UnitType


class Item(Entity):
    code: int
    name: str
    leadtime: float


class ItemStock(Quantifiable):
    item: Item


class Mixer(Entity, Quantifiable):
    speed: float
    changeover_time: float


class RecipeIngredient(BaseModel, Quantifiable):
    item: Item
    type: IngredientType


class Recipe(Entity):
    process_yield: float
    description: str = Field(default="", max_length=255)
    ingredients: list[RecipeIngredient]


class PurchasingPlan(DateTimeObject, Quantifiable):
    item: Item
    supplier: str


class ShipmentPlan(DateTimeObject, Quantifiable):
    item: Item
    client: str


class ProcurementPlan(DateTimeObject, Quantifiable):
    item: Item
    working_hours: float
