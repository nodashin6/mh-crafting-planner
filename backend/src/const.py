from pathlib import Path

BACKEND_DIR = Path(__file__).parent.parent
DATA_DIR = BACKEND_DIR / "data"
CSV_DIR = DATA_DIR / "csv"
JSON_DIR = DATA_DIR / "json"

MASTER_CSV_DIR = CSV_DIR / "master"
TRANSACTION_CSV_DIR = CSV_DIR / "transaction"
