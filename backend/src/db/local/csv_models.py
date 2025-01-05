from abc import ABC
from datetime import date, time
from pydantic import BaseModel
from typing import Type, Dict


class CsvModelType(BaseModel, ABC):
    pass


class ItemCsv(CsvModelType):
    code: int
    name: str
    leadtime: float


class MixerCsv(CsvModelType):
    code: int
    name: str
    capacity: int
    speed: float
    changeover_time: float


class RecipeCsv(CsvModelType):
    input1: str
    input2: str
    output: str
    process_yield: float


class PurchasingPlanCsv(CsvModelType):
    code: int
    date: date
    time: time
    item_code: int
    weight: int
    supplier: str


class ShipmentPlanCsv(CsvModelType):
    code: int
    date: date
    time: time
    item_code: int
    weight: int
    client: str


class MasterDataCsv(BaseModel):
    items: list[ItemCsv]
    mixers: list[MixerCsv]
    recipes: list[RecipeCsv]


class TransactionDataCsv(BaseModel):
    purchasing_plans: list[PurchasingPlanCsv]
    shipment_plans: list[ShipmentPlanCsv]
