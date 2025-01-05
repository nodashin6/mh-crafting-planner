from .csv_models import (
    CsvModelType,
    ItemCsv,
    MixerCsv,
    RecipeCsv,
    PurchasingPlanCsv,
    ShipmentPlanCsv,
    MasterDataCsv,
    TransactionDataCsv,
)
from ...models import Item, Mixer, Recipe, PurchasingPlan, ShipmentPlan, Master


class MasterTransformer:
    def __init__(self, master_csv: MasterDataCsv):
        self.master_csv = master_csv


class TransactionTransformer:
    def __init__(self, transaction: TransactionDataCsv):
        self.transaction = transaction
