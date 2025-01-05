from pydantic import BaseModel, Field
from .base import BaseEntity
from ..types import IngredientType, UnitType


class Recipe(BaseEntity):
    process_yield: float
    description: str = Field(default="", max_length=255)


class RecipeIngredient(BaseModel):
    recipe_code: int
    item_code: int
    quantity: int
    unit: UnitType
    type: IngredientType


class RecipeCsv(BaseModel):
    input1: str
    input2: str
    output: str
    process_yield: float
