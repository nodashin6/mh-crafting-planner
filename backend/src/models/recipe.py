from pydantic import BaseModel, Field
from .base import BaseEntity
from ..types import IngredientType


class Recipe(BaseEntity):
    process_yield: float
    description: str = Field(default="", max_length=255)


class RecipeIngredient(BaseModel):
    recipe_code: int
    item_code: int
    quantity: int
    unit: str
    type: IngredientType
