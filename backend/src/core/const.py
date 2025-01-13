from pathlib import Path

REPOSITORY_DIR = Path(__file__).parent.parent.parent
BACKEND_DIR = Path(__file__).parent.parent
DATA_DIR = REPOSITORY_DIR / "storage" / "data"
CSV_DIR = DATA_DIR / "csv"
JSON_DIR = DATA_DIR / "json"

MASTER_CSV_DIR = CSV_DIR / "master"
TRANSACTION_CSV_DIR = CSV_DIR / "transaction"
