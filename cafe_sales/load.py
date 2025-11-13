from pathlib import Path
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def load_data(df: pd.DataFrame, output_dir: Path, filename: str = "clean_sales.csv"):
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / filename
    df.to_csv(output_file, index=False)
    logger.info(f"✅ Dados salvos com sucesso em: {output_file}")