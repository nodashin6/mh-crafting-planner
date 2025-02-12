from supabase import Client
from src.core.supabase import create_supabase_client, tables
from src.core.domain import models


def test_create_supabase_client():
    client = create_supabase_client()
    assert isinstance(client, Client)


def test_get_all_items():
    client = create_supabase_client()
    data = client.table("items").select("*").execute().data
    assert isinstance(data, list)
    item = data[0]
    assert "id" in item
    assert "name" in item
    assert "leadtime" in item
    assert "price" in item


def test_item_table_as_entity():
    client = create_supabase_client()
    data = client.table("items").select("*").execute().data
    assert isinstance(data, list)
    items = [tables.ItemTable(item).as_entity() for item in data]
    assert isinstance(items, list)
    assert isinstance(items[0], models.Item)


def test_mixers_table_as_entity():
    client = create_supabase_client()
    data = client.table("mixers").select("*").execute().data
    assert isinstance(data, list)
    mixers = [tables.MixserTable(mixer).as_entity() for mixer in data]
    assert isinstance(mixers, list)
    assert isinstance(mixers[0], models.Mixer)


def test_precursors_table_as_entity():
    client = create_supabase_client()
    data = client.table("precursors").select("*, items(*)").execute().data
    assert isinstance(data, list)
    precursors = [tables.PrecursorTable(precursor).as_entity() for precursor in data]
    assert isinstance(precursors, list)
    assert isinstance(precursors[0], models.Precursor)


def test_products_table_as_entity():
    client = create_supabase_client()
    data = client.table("products").select("*, items(*)").execute().data
    assert isinstance(data, list)
    products = [tables.ProductTable(product).as_entity() for product in data]
    assert isinstance(products, list)
    assert isinstance(products[0], models.Product)


def test_crafts_table_as_entity():
    client = create_supabase_client()
    data = (
        client.table("crafts")
        .select("*, products(*, items(*)), precursors(*, items(*))")
        .execute()
        .data
    )
    assert isinstance(data, list)
    crafts = [tables.CraftTable(craft).as_entity() for craft in data]
    assert isinstance(crafts, list)
    assert isinstance(crafts[0], models.Craft)
    assert isinstance(crafts[0].product, models.Product)
    assert isinstance(crafts[0].precursors, list)
    assert isinstance(crafts[0].precursors[0], models.Precursor)


def test_players_table_as_entity():
    client = create_supabase_client()
    data = client.table("players").select("*").execute().data
    assert isinstance(data, list)
    players = [tables.PlayerTable(player).as_entity() for player in data]
    assert isinstance(players, list)
    assert isinstance(players[0], models.Player)


def test_savedatas_table_as_entity():
    client = create_supabase_client()
    data = client.table("savedatas").select("*, players(*)").execute().data
    assert isinstance(data, list)
    savedatas = [tables.SavedataTable(savedata).as_entity() for savedata in data]
    assert isinstance(savedatas, list)
    assert isinstance(savedatas[0], models.Savedata)
    assert isinstance(savedatas[0].player, models.Player)


def test_belongs_table_as_entity():
    client = create_supabase_client()
    data = (
        client.table("belongings")
        .select("*, items(*), savedatas(*, players(*))")
        .execute()
        .data
    )
    print(f"{data=}")
    assert isinstance(data, list)
    belongs = [tables.BelongingTable(belong).as_entity() for belong in data]
    assert isinstance(belongs, list)
    assert isinstance(belongs[0], models.Belonging)
    assert isinstance(belongs[0].item, models.Item)


def test_facilities_table_as_entity():
    client = create_supabase_client()
    data = (
        client.table("facilities")
        .select("*, savedatas(*, players(*)), mixers(*)")
        .execute()
        .data
    )
    assert isinstance(data, list)
    facilities = [tables.FacilityTable(facility).as_entity() for facility in data]
    assert isinstance(facilities, list)
    # assert isinstance(facilities[0], models.Facility)
    # assert isinstance(facilities[0].mixser, models.Mixser)
