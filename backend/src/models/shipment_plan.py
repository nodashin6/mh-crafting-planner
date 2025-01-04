from pydantic import BaseModel
from datetime import datetime
from base import BaseItemWeightPlan


class ShipmentPlan(BaseItemWeightPlan):
    client: str
