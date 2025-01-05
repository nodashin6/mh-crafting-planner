from pydantic import BaseModel
from .base import BaseEntity, BaseQuantifiable


class Mixer(BaseEntity, BaseQuantifiable):
    speed: float
    changeover_time: float
