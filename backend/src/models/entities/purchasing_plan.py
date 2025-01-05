from pydantic import BaseModel
from .base import BasePlan, BaseQuantifiable
from .item import Item


class PurchasingPlan(BasePlan, BaseQuantifiable):
    item: Item
    supplier: str
