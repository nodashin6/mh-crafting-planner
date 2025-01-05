from pydantic import BaseModel
from datetime import datetime, time
from .base import BasePlan, BaseQuantifiable
from .item import Item


class ProcurementPlan(BasePlan, BaseQuantifiable):
    item: Item
    working_hours: float
