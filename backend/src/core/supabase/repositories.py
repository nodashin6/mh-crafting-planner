from abc import ABC, abstractmethod

from supabase import Client
from src.core.domain.base_repository import BaseRepository
from src.core.domain import models
from . import tables
from typing import List, Dict, Generic, TypeVar


class BaseSupabaseRepository:

    def __init__(self, client: Client):
        self.client = client


class ItemRepository(BaseRepository[models.Item], BaseSupabaseRepository):

    def read_all(self):
        data = self.client.table("items").select("*").execute().data
        return [tables.ItemTable(item).as_entity() for item in data]


class MixerRepository(BaseRepository[models.Mixer], BaseSupabaseRepository):

    def read_all(self):
        data = self.client.table("mixers").select("*").execute().data
        return [tables.MixserTable(mixer).as_entity() for mixer in data]


class PrecursorRepository(BaseRepository[models.Precursor], BaseSupabaseRepository):

    def read_all(self):
        data = self.client.table("precursors").select("*, items(*)").execute().data
        return [tables.PrecursorTable(precursor).as_entity() for precursor in data]


class ProductRepository(BaseRepository[models.Product], BaseSupabaseRepository):

    def read_all(self):
        data = self.client.table("products").select("*, items(*)").execute().data
        return [tables.ProductTable(product).as_entity() for product in data]


class CraftRepository(BaseRepository[models.Craft], BaseSupabaseRepository):

    def read_all(self):
        data = (
            self.client.table("crafts")
            .select("*, products(*), precursors(*)")
            .execute()
            .data
        )
        return [tables.CraftTable(craft).as_entity() for craft in data]


class PlayerRepository(BaseRepository[models.Player], BaseSupabaseRepository):

    def read_all(self):
        data = self.client.table("players").select("*").execute().data
        return [tables.PlayerTable(player).as_entity() for player in data]


class SavedataRepository(BaseRepository[models.Savedata], BaseSupabaseRepository):

    def read_all(self):
        data = self.client.table("savedata").select("*, player(*)").execute().data
        return [tables.SavedataTable(savedata).as_entity() for savedata in data]


class BelongingRepository(BaseRepository[models.Belonging], BaseSupabaseRepository):

    def read_all(self):
        data = self.client.table("belongings").select("*, item(*)").execute().data
        return [tables.BelongingTable(belonging).as_entity() for belonging in data]
