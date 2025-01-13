from abc import ABC, abstractmethod
from typing import List, TypeVar, Generic
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)

class BaseController(ABC, Generic[T]):
    @abstractmethod
    def create(self, item: T) -> T:
        pass

    @abstractmethod
    def read(self, item_id: int) -> T:
        pass

    @abstractmethod
    def update(self, item_id: int, item: T) -> T:
        pass

    @abstractmethod
    def delete(self, item_id: int) -> None:
        pass

    @abstractmethod
    def list(self) -> List[T]:
        pass
