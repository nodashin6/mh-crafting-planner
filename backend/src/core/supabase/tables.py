from abc import ABC, abstractmethod
from typing import List, Dict, Generic, TypeVar
from pydantic import BaseModel

from src.core.domain import models


T = TypeVar("T", bound=models.BaseEntity)


class BaseTable(ABC, Generic[T]):

    def __init__(self, data: Dict):
        self._data = data

    @property
    def data(self):
        return self._data

    @abstractmethod
    def as_entity(self) -> BaseModel:
        return self._data


class ItemTable(BaseTable[models.Item]):

    def as_entity(self) -> models.Item:
        return models.Item(
            id=self._data["id"],
            name=self._data["name"],
            leadtime=self._data["leadtime"],
            price=self._data["price"],
        )


class MixserTable(BaseTable[models.Mixer]):

    def as_entity(self) -> models.Mixer:
        return models.Mixer(
            id=self._data["id"],
            max_capacity=self._data["max_capacity"],
            changeover_hours=self._data["changeover_hours"],
        )


class PrecursorTable(BaseTable[models.Precursor]):

    @property
    def item(self) -> models.Item:
        return ItemTable(self._data["items"]).as_entity()

    def as_entity(self) -> models.Precursor:
        return models.Precursor(
            id=self._data["id"],
            item=self.item,
        )


class ProductTable(BaseTable[models.Product]):

    @property
    def item(self) -> models.Item:
        return ItemTable(self._data["items"]).as_entity()

    def as_entity(self) -> models.Product:
        return models.Product(
            id=self._data["id"],
            item=self.item,
        )


class CraftTable(BaseTable[models.Craft]):

    @property
    def product(self) -> models.Product:
        products = [ProductTable(p).as_entity() for p in self._data["products"]]
        assert len(products) == 1
        return products[0]

    @property
    def precursors(self) -> List[models.Precursor]:
        return [PrecursorTable(p).as_entity() for p in self._data["precursors"]]

    def as_entity(self) -> models.Craft:
        return models.Craft(
            id=self._data["id"],
            required_hours=self._data["required_hours"],
            yield_=self._data["yield"],
            product=self.product,
            precursors=self.precursors,
        )


class PlayerTable(BaseTable[models.Player]):

    def as_entity(self) -> models.Player:
        return models.Player(
            id=self._data["id"],
            name=self._data["name"],
        )


class SavedataTable(BaseTable[models.Savedata]):

    @property
    def player(self) -> models.Player:
        return PlayerTable(self._data["players"]).as_entity()

    def as_entity(self) -> models.Savedata:
        return models.Savedata(
            id=self._data["id"],
            player=self.player,
            gold=self._data["gold"],
            current_day=self._data["current_day"],
            current_hour=self._data["current_hour"],
        )


class BelongingTable(BaseTable[models.Belonging]):

    @property
    def savedata(self) -> models.Savedata:
        return SavedataTable(self._data["savedatas"]).as_entity()

    @property
    def item(self) -> models.Item:
        return ItemTable(self._data["items"]).as_entity()

    def as_entity(self) -> models.Belonging:
        return models.Belonging(
            id=self._data["id"],
            savedata=self.savedata,
            item=self.item,
            quantity=self._data["quantity"],
        )


class FacilityTable(BaseTable[models.Facility]):

    @property
    def savedata(self) -> models.Savedata:
        return SavedataTable(self._data["savedatas"]).as_entity()

    @property
    def mixser(self) -> models.Mixer:
        return MixserTable(self._data["mixsers"]).as_entity()

    def as_entity(self) -> models.Facility:
        return models.Facility(
            id=self._data["id"],
            name=self._data["name"],
            savedata=self.savedata,
            mixser=self.mixser,
        )


class ScheduleTable(BaseTable[models.Schedule]):

    @property
    def savedata(self) -> models.Savedata:
        return SavedataTable(self._data["savedatas"]).as_entity()

    @property
    def craft(self) -> models.Craft:
        return CraftTable(self._data["crafts"]).as_entity()

    def as_entity(self) -> models.Schedule:
        return models.Schedule(
            id=self._data["id"],
            savedata=self.savedata,
            craft=self.craft,
            start_day=self._data["start_day"],
            start_hour=self._data["start_hour"],
            end_day=self._data["end_day"],
            end_hour=self._data["end_hour"],
            has_completed=self._data["has_completed"],
        )


class OrderTable(BaseTable[models.Order]):
    @property
    def savedata(self) -> models.Savedata:
        return SavedataTable(self._data["savedatas"]).as_entity()

    @property
    def product(self) -> models.Product:
        return ProductTable(self._data["products"]).as_entity()

    def as_entity(self) -> models.Order:
        return models.Order(
            id=self._data["id"],
            savedata=self.savedata,
            product=self.product,
            quantity=self._data["quantity"],
            due_day=self._data["due_day"],
        )


class MessageTable(BaseTable[models.Message]):
    @property
    def savedata(self) -> models.Savedata:
        return SavedataTable(self._data["savedatas"]).as_entity()

    def as_entity(self) -> models.Message:
        return models.Message(
            id=self._data["id"],
            savedata=self.savedata,
            day=self._data["day"],
            hour=self._data["hour"],
        )
