from pathlib import Path
from cafe_sales.pipeline import run_pipeline
from cafe_sales.load import load_data

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "data" / "output"

if __name__ == "__main__":
    run_pipeline()