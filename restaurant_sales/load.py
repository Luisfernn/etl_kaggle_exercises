from pathlib import Path
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.propagate = False

def load_data(df: pd.DataFrame, file_name: str = "restautant_sales_clean.csv", overwrite: bool = True):

     output_dir = Path(__file__).resolve().parent / "data" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)

    file_path = output_dir / file_name
