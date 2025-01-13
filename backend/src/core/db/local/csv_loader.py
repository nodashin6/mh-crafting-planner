from abc import ABC, abstractmethod
import pandas as pd
from pydantic import BaseModel, Field
from typing import Type, Generic, TypeVar, Iterator, Callable
from pathlib import Path
from dataclasses import dataclass
from datetime import date, time

from .csv_interface import (
    CsvAdapter,
    CsvAdapterColumn,
    CsvLoaderConfig,
    BaseCsvLoader,
    T,
    MASTER_CSV_DIR,
    TRANSACTION_CSV_DIR,
    BaseMasterCsvLoader,
    BaseTransactionCsvLoader,
)

from .csv_models import (
    ItemCsv,
    MixerCsv,
    RecipeCsv,
    PurchasingPlanCsv,
    ShipmentPlanCsv,
    MasterDataCsv,
    TransactionDataCsv,
)


#
# Implementation
#
ITEM_CSV_LOADER_CONFIG = CsvLoaderConfig(
    save_dir=MASTER_CSV_DIR,
    basename="items",
    adapter=CsvAdapter(
        ModelType=ItemCsv,
        columns={
            "code": CsvAdapterColumn("Code", int),
            "name": CsvAdapterColumn("Name", str),
            "leadtime": CsvAdapterColumn("Leadtime", float),
        },
    ),
)

MIXER_CSV_LOADER_CONFIG = CsvLoaderConfig(
    save_dir=MASTER_CSV_DIR,
    basename="mixers",
    adapter=CsvAdapter(
        ModelType=MixerCsv,
        columns={
            "code": CsvAdapterColumn("Code", int),
            "name": CsvAdapterColumn("Name", str),
            "capacity": CsvAdapterColumn("Capacity", int),
            "speed": CsvAdapterColumn("Speed", float),
            "changeover_time": CsvAdapterColumn("ChangeoverTime", float),
        },
    ),
)

RECIPE_CSV_LOADER_CONFIG = CsvLoaderConfig(
    save_dir=MASTER_CSV_DIR,
    basename="recipes",
    adapter=CsvAdapter(
        ModelType=RecipeCsv,
        columns={
            "input1": CsvAdapterColumn("Input1", str),
            "input2": CsvAdapterColumn("Input2", str),
            "output": CsvAdapterColumn("Output", str),
            "process_yield": CsvAdapterColumn("Yield", float),
        },
    ),
)

PURCHASE_PLAN_CSV_LOADER_CONFIG = CsvLoaderConfig(
    save_dir=TRANSACTION_CSV_DIR,
    basename="purchasing_plan",
    adapter=CsvAdapter(
        ModelType=PurchasingPlanCsv,
        columns={
            "code": CsvAdapterColumn("Code", int),
            "date": CsvAdapterColumn("Date", str),
            "time": CsvAdapterColumn("Time", str),
            "item_code": CsvAdapterColumn("ItemCode", int),
            "weight": CsvAdapterColumn("Weight", int),
            "supplier": CsvAdapterColumn("Supplier", str),
        },
    ),
)

SHIPMENT_PLAN_CSV_LOADER_CONFIG = CsvLoaderConfig(
    save_dir=TRANSACTION_CSV_DIR,
    basename="shipment_plan",
    adapter=CsvAdapter(
        ModelType=ShipmentPlanCsv,
        columns={
            "code": CsvAdapterColumn("Code", int),
            "date": CsvAdapterColumn("Date", str),
            "time": CsvAdapterColumn("Time", str),
            "item_code": CsvAdapterColumn("ItemCode", int),
            "weight": CsvAdapterColumn("Weight", int),
            "client": CsvAdapterColumn("Client", str),
        },
    ),
)


class ItemCsvLoader(BaseCsvLoader, Generic[T]):

    def __init__(self, config=ITEM_CSV_LOADER_CONFIG):
        super().__init__(config)


class MixedCsvLoader(BaseCsvLoader, Generic[T]):

    def __init__(self, config=MIXER_CSV_LOADER_CONFIG):
        super().__init__(config)


class RecipeCsvLoader(BaseCsvLoader, Generic[T]):

    def __init__(self, config=RECIPE_CSV_LOADER_CONFIG):
        super().__init__(config)


class PurchasingPlanCsvLoader(BaseCsvLoader, Generic[T]):
    def __init__(self, config=PURCHASE_PLAN_CSV_LOADER_CONFIG):
        super().__init__(config)


class ShipmentPlanCsvLoader(BaseCsvLoader, Generic[T]):
    def __init__(self, config=SHIPMENT_PLAN_CSV_LOADER_CONFIG):
        super().__init__(config)


class MasterCsvLoader(BaseMasterCsvLoader):
    def __init__(self):
        pass

    def load(self) -> MasterDataCsv:
        items = ItemCsvLoader().load()
        mixers = MixedCsvLoader().load()
        recipes = RecipeCsvLoader().load()
        return MasterDataCsv(items=items, mixers=mixers, recipes=recipes)


class TransactionCsvLoader(BaseTransactionCsvLoader):
    def __init__(self):
        pass

    def load(self) -> TransactionDataCsv:
        purchasing_plans = PurchasingPlanCsvLoader().load()
        shipment_plans = ShipmentPlanCsvLoader().load()
        return TransactionDataCsv(
            purchasing_plans=purchasing_plans, shipment_plans=shipment_plans
        )
