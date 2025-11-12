from pathlib import Path
import pandas as pd

import logging

logger = logging.getLogger(__name__)

def extract_data(file_path: Path = None):

    if file_path is None:
        base_dir = Path(__file__).resolve().parent
        file_path = base_dir / "data" / "input" / "dirty_cafe_sales.csv"

    if not file_path.exists():
        logger.error(f"❌ Arquivo não encontrado: {file_path}")
        return None

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        logger.error(f"⚠️ Erro ao ler o arquivo: {e}")
        return None

    logger.info(f"\n✅ Arquivo carregado com sucesso: {file_path.name}")
    logger.info(f"📊 Linhas: {len(df)}, Colunas: {len(df.columns)}\n")

    logger.info("Prévia dos dados (10 primeiras linhas):")
    logger.info(f"{df.head(10)}\n")

    logger.info("Prévia das últimas 10 linhas:")
    logger.info(f"{df.tail(10)}\n")

    return df

if __name__ == "__main__":
    
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(message)s")
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    extract_data()