from .entities import (
    Item,
    Mixer,
    Recipe,
    RecipeIngredient,
    ProcurementPlan,
    PurchasingPlan,
    ShipmentPlan,
)
from .master import Master
from pydantic import BaseModel


class MaterialTransaction(BaseModel):
    purchasing_plans: list[PurchasingPlan]
    shipment_plans: list[ShipmentPlan]


class Shedule(BaseModel):
    procurement_plans: list[ProcurementPlan]
