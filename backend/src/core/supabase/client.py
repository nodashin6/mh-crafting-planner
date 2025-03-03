import os

from supabase import create_client, Client

SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")


def create_supabase_client() -> Client:
    return create_client(SUPABASE_URL, SUPABASE_KEY)