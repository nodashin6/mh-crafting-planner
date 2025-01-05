from pydantic import BaseModel
from .base import BaseEntity

class Item(BaseEntity):
    code: int
    name: str
    leadtime: float
