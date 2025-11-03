from pathlib import Path
import pandas as pd

import logging

logger = logging.getLogger(__name__)
logger.propagate = False 
logger.addHandler(logging.NullHandler())

def extract_data(file_path: Path = None):

    if file_path is None:
        base_dir = Path(__file__).resolve().parent
        file_path = base_dir / "data" / "input" / "dirty_cafe_sales.csv"

    df = pd.read_csv(file_path)     

    logger.info(f"\n✅ Arquivo carregado com sucesso: {file_path.name}")
    logger.info(f"📊 Linhas: {len(df)}, Colunas: {len(df.columns)}\n")

    logger.info("Prévia dos dados (10 primeiras linhas):")
    logger.info(f"{df.head(10)}\n")

    logger.info("Prévia das últimas 10 linhas:")
    logger.info(f"{df.tail(10)}\n")

    return df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    extract_data()