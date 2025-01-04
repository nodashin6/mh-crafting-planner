from pydantic import BaseModel
from datetime import datetime, time
from .base import BaseItemWeightPlan


class ProcurementPlan(BaseItemWeightPlan):
    working_hours: float
