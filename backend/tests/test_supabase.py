import os
from supabase import create_client, Client

from src.core.supabase import create_supabase_client


def test_fetch_items():
    client = create_supabase_client()
    response = client.table("items").select("*").execute()
    assert 0 < len(response.data)
