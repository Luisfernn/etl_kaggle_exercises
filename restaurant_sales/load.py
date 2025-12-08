from pathlib import Path
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.propagate = False

def load_data(df: pd.DataFrame, file_name: str = "restautant_sales_clean.csv", overwrite: bool = True):
