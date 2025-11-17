import logging
from pathlib import Path
from cafe_sales.pipeline import run_pipeline
from cafe_sales.load import load_data

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "data" / "output"

LOG_DIR = BASE_DIR / "data" / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(OUTPUT_DIR / "etl.log", mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

if __name__ == "__main__":
    df = run_pipeline()

    if df is not None:
        load_data(df, OUTPUT_DIR)