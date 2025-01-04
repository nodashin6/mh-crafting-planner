from pydantic import BaseModel
from .base import BaseEntity


class Item(BaseEntity):
    leadtime: float
