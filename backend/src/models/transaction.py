from .entities import (
    Item,
    Mixer,
    Recipe,
    RecipeIngredient,
    ProcurementPlan,
    PurchasingPlan,
    ShipmentPlan,
)
from .master import CraftingMaster
from pydantic import BaseModel


class ItemTransaction(BaseModel):
    purchasing_plans: list[PurchasingPlan]
    shipment_plans: list[ShipmentPlan]


class CraftSchedule(BaseModel):
    procurement_plans: list[ProcurementPlan]
