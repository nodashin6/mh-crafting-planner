from abc import ABC, abstractmethod
import pandas as pd
from pydantic import BaseModel, Field
from typing import Type, Generic, TypeVar, Iterator, Callable, Dict, Tuple, NamedTuple
from pathlib import Path
from dataclasses import dataclass
from datetime import date, time
from .csv_models import CsvModelType
from ...const import MASTER_CSV_DIR, TRANSACTION_CSV_DIR

#
# Config And Adapter
#
T = TypeVar("T", bound=CsvModelType)


class CsvAdapterColumn(NamedTuple):
    column: str
    dtype: Type


class CsvAdapter(BaseModel, Generic[T]):
    ModelType: Type[T]
    columns: Dict[str, CsvAdapterColumn]


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
