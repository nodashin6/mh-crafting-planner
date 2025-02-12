from . import models

from abc import ABC, abstractmethod
from typing import List, Dict, Generic, TypeVar


T = TypeVar("T", bound=models.BaseEntity)
U = TypeVar("U")


class __BaseRepository(ABC, Generic[T, U]):
    """最終的なベースリポジトリクラス"""

    @abstractmethod
    def read(self, id: int) -> T:
        pass

    @abstractmethod
    def read_all(self) -> List[T]:
        pass

    @abstractmethod
    def create(self, entity: U) -> T:
        pass

    @abstractmethod
    def update(self, entity: U) -> T:
        pass

    @abstractmethod
    def delete(self, id: int) -> T:
        pass


class BaseRepository(ABC, Generic[T]):
    """開発初期段階のベースリポジトリクラス"""

    @abstractmethod
    def read_all(self) -> List[T]:
        pass
