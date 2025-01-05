from pydantic import BaseModel
from datetime import datetime
from .base import BasePlan, BaseQuantifiable
from .item import Item


class ShipmentPlan(BasePlan, BaseQuantifiable):
    item: Item
    client: str
