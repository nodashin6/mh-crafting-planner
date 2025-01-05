from pydantic import BaseModel, Field
from .base import BaseEntity, BaseQuantifiable
from ...types import IngredientType, UnitType
from .item import Item


class RecipeIngredient(BaseModel, BaseQuantifiable):
    item: Item
    type: IngredientType


class Recipe(BaseEntity):
    process_yield: float
    description: str = Field(default="", max_length=255)
    ingredients: list[RecipeIngredient]
