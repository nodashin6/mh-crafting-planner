import os
from supabase import create_client, Client

def test_client():
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    assert url is not None, "SUPABASE_URL environment variable is not set"
    assert key is not None, "SUPABASE_KEY environment variable is not set"
    supabase: Client = create_client(url, key)
    response = supabase.rpc('ping').execute()
    assert response.data == 'pong'
    
    
def test_utils_client():
    from src.core.utils.supabase.client import supabase_client
    supabase = supabase_client()
    response = supabase.rpc('ping').execute()
    assert response.data == 'pong'

url = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def test_fetch_items():
    response = supabase.table("items").select("*").execute()
    assert 0 < len(response.data)


def test_fetch_mixers():
    response = supabase.table("mixers").select("*").execute()
    assert 0 < len(response.data)


def test_fetch_recipes():
    response = supabase.table("recipes").select("*").execute()
    assert 0 < len(response.data)