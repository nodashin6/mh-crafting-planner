from src.core.supabase import repositories
from src.core.supabase import create_supabase_client


def test_item_repository():
    client = create_supabase_client()
    item_repository = repositories.ItemRepository(client)
    items = item_repository.read_all()
    assert len(items) > 0


def test_mixer_repository():
    client = create_supabase_client()
    mixer_repository = repositories.MixerRepository(client)
    mixers = mixer_repository.read_all()
    assert len(mixers) > 0
