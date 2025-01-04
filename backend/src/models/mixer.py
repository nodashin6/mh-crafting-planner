from pydantic import BaseModel
from .base import BaseEntity

class Mixer(BaseEntity):
    capacity: int
    speed: float
    changeover_time: float
