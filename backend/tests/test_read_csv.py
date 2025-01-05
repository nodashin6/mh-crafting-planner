from datetime import date, time

from src.db.local.csv_loader import (
    ItemCsvLoader,
    MixedCsvLoader,
    RecipeCsvLoader,
    PurchasingPlanCsvLoader,
    ShipmentPlanCsvLoader,
    MasterCsvLoader,
    MasterDataCsv,
    TransactionCsvLoader,
    TransactionDataCsv,
)


def test_item_csv_loader():
    loader = ItemCsvLoader()
    items = loader.load()
    assert 0 < len(items)
    item = items[0]
    assert isinstance(item.code, int)
    assert isinstance(item.name, str)
    assert isinstance(item.leadtime, float)


def test_mixer_csv_loader():
    loader = MixedCsvLoader()
    mixers = loader.load()
    assert 0 < len(mixers)
    mixer = mixers[0]
    assert isinstance(mixer.code, int)
    assert isinstance(mixer.name, str)
    assert isinstance(mixer.capacity, int)
    assert isinstance(mixer.speed, float)
    assert isinstance(mixer.changeover_time, float)


def test_recipe_csv_loader():
    loader = RecipeCsvLoader()
    recipes = loader.load()
    assert 0 < len(recipes)
    recipe = recipes[0]
    assert isinstance(recipe.input1, str)
    assert isinstance(recipe.input2, str)
    assert isinstance(recipe.output, str)
    assert isinstance(recipe.process_yield, float)


def test_purchasing_plan_csv_loader():
    loader = PurchasingPlanCsvLoader()
    purchasing_plans = loader.load()
    assert 0 < len(purchasing_plans)
    purchasing_plan = purchasing_plans[0]
    assert isinstance(purchasing_plan.code, int)
    assert isinstance(purchasing_plan.date, date)
    assert isinstance(purchasing_plan.time, time)
    assert isinstance(purchasing_plan.item_code, int)
    assert isinstance(purchasing_plan.weight, int)
    assert isinstance(purchasing_plan.supplier, str)


def test_shipment_plan_csv_loader():
    loader = ShipmentPlanCsvLoader()
    shipment_plans = loader.load()
    assert 0 < len(shipment_plans)
    shipment_plan = shipment_plans[0]
    assert isinstance(shipment_plan.code, int)
    assert isinstance(shipment_plan.date, date)
    assert isinstance(shipment_plan.time, time)
    assert isinstance(shipment_plan.item_code, int)
    assert isinstance(shipment_plan.weight, int)
    assert isinstance(shipment_plan.client, str)


def test_master_csv_loader():
    loader = MasterCsvLoader()
    master_data = loader.load()
    assert isinstance(master_data, MasterDataCsv)
    assert 0 < len(master_data.items)
    assert 0 < len(master_data.mixers)
    assert 0 < len(master_data.recipes)


def test_transaction_csv_loader():
    loader = TransactionCsvLoader()
    transaction_data = loader.load()
    assert isinstance(transaction_data, TransactionDataCsv)
    assert 0 < len(transaction_data.purchasing_plans)
    assert 0 < len(transaction_data.shipment_plans)
