from pathlib import Path
from cafe_sales.pipeline import run_pipeline
from cafe_sales.load import load_data

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "data" / "output"

if __name__ == "__main__":
    df = run_pipeline()

    if df is not None:
        load_data(df, OUTPUT_DIR)