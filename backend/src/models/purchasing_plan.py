from pydantic import BaseModel
from .base import BaseItemWeightPlan


class PurchasingPlan(BaseItemWeightPlan):
    supplier: str
