from pydantic import BaseModel, Field
from datetime import date, time
from ...base.domain.entities import NamedEntity, DateTimeObject, Quantifiable
from ...base.types import IngredientType, UnitType



class Item(NamedEntity):
    code: int
    leadtime: float


class Mixser(NamedEntity, Quantifiable):
    code: int
    speed: float
    changeover_time: float
    
    
class RecipeIngredient(Quantifiable, BaseModel):
    item: Item
    type: IngredientType



class Recipe(Entity):
    process_yield: float
    description: str = Field(default="", max_length=255)
    ingredients: list[RecipeIngredient]