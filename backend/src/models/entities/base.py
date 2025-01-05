from pydantic import BaseModel
from datetime import date, time
from ...types.unit import UnitType


class BaseEntity(BaseModel):
    code: int
    name: str


class BasePlan(BaseModel):
    code: int
    date: date
    time: time


class BaseQuantifiable(BaseModel):
    quantity: float
    unit: UnitType
