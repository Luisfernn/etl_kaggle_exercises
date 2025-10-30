from pathlib import Path
import pandas as pd

import logging

logger = logging.getLogger(__name__)
logger.propagate = False  # impede o logger de enviar mensagens ao root
logger.addHandler(logging.NullHandler())

def extract_data(file_path: Path = None):

    if file_path is None:
        base_dir = Path(__file__).resolve().parent
        file_path = base_dir / "data" / "input" / "dirty_cafe_sales.csv"

    df = pd.read_csv(file_path)     

    logging.info(f"\n✅ Arquivo carregado com sucesso: {file_path.name}")
    logging.info(f"📊 Linhas: {len(df)}, Colunas: {len(df.columns)}\n")

    logging.info("Prévia dos dados (10 primeiras linhas):")
    logging.info(f"{df.head(10)}\n")

    logging.info("Prévia das últimas 10 linhas:")
    logging.info(f"{df.tail(10)}\n")

    return df

if __name__ == "__main__":
    extract_data()