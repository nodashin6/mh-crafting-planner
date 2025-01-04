import sys
from pathlib import Path

# Add the src directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))

from src.db.local.csv_loader import ItemCsvLoader, MixedCsvLoader


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
