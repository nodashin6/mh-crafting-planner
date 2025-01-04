from abc import ABC, abstractmethod
import pandas as pd
from pydantic import BaseModel, Field
from typing import Type, Generic, TypeVar, Iterator
from pathlib import Path
from dataclasses import dataclass

from ...const import MASTER_CSV_DIR, TRANSACTION_CSV_DIR
from ...models import Item, Mixer


#
# Config And Adapter
#
T = TypeVar("T", bound=BaseModel)


class CsvAdapterColumn(BaseModel):
    column: str
    dtype: Type


class CsvAdapter(BaseModel, Generic[T]):
    ModelType: Type[T]
    columns: dict[str, CsvAdapterColumn]


def CsvAdapterInterface(
    ModelType: Type[T], columns: dict[str, tuple[str, Type]]
) -> CsvAdapter[T]:
    """create CsvAdapter instance

    Args:
        ModelType (Type[T]): ...
        columns (dict[str, tuple[str, Type]]): ...

    Returns:
        CsvAdapter[T]: ...
    """
    adapter_columns = {}
    for key, value in columns.items():
        adapter_columns[key] = CsvAdapterColumn(column=value[0], dtype=value[1])
    return CsvAdapter[T](ModelType=ModelType, columns=adapter_columns)


class CsvLoaderConfig(BaseModel):
    save_dir: Path
    basename: str
    encoding: str = Field("utf-8")
    adapter: CsvAdapter[T] = Field(None)


def adapt(row: pd.Series, adapter: CsvAdapter[T]) -> T:
    kwargs = {}
    for key, value in adapter.columns.items():
        kwargs[key] = value.dtype(row[value.column])
    return adapter.ModelType(**kwargs)


#
# CsvLoader
#
class BaseCsvLoader(ABC, Generic[T]):

    def __init__(self, config: CsvLoaderConfig):
        self.config = config

    @property
    def csv_path(self) -> Path:
        return (self.config.save_dir / self.config.basename).with_suffix(".csv")

    def read(self) -> pd.DataFrame:
        return pd.read_csv(self.csv_path, encoding=self.config.encoding)

    def __iter__(self) -> Iterator[T]:
        df = self.read()
        for _, row in df.iterrows():
            yield self._adapt(row)

    def load(self) -> list[T]:
        return list(self)

    def _adapt(self, row: pd.Series) -> T:
        return adapt(row, self.config.adapter)


#
# Implementation
#
ITEM_CSV_LOADER_CONFIG = CsvLoaderConfig(
    save_dir=MASTER_CSV_DIR,
    basename="items",
    adapter=CsvAdapterInterface(
        ModelType=Item,
        columns={
            "code": ("Code", int),
            "name": ("Name", str),
            "leadtime": ("Leadtime", float),
        },
    ),
)

MIXER_CSV_LOADER_CONFIG = CsvLoaderConfig(
    save_dir=MASTER_CSV_DIR,
    basename="mixers",
    adapter=CsvAdapterInterface(
        ModelType=Mixer,
        columns={
            "code": ("Code", int),
            "name": ("Name", str),
            "capacity": ("Capacity", int),
            "speed": ("Speed", float),
            "changeover_time": ("ChangeoverTime", float),
        },
    ),
)


class ItemCsvLoader(BaseCsvLoader, Generic[T]):

    def __init__(self, config=ITEM_CSV_LOADER_CONFIG):
        super().__init__(config)


class MixedCsvLoader(BaseCsvLoader, Generic[T]):

    def __init__(self, config=MIXER_CSV_LOADER_CONFIG):
        super().__init__(config)
