from pydantic import BaseModel
from datetime import date, time


class BaseEntity(BaseModel):
    code: int
    name: str


class BasePlan(BaseModel):
    code: int
    date: date
    time: time


class BaseItemWeightPlan(BasePlan):
    item_code: int
    weight: int
