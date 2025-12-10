from pathlib import Path
import pandas as pd

import logging

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())
logger.propagate = False

def extract_data(file_path: Path = None):

    if file_path is None:
        base_dir = Path(__file__).resolve().parent
        file_path = base_dir / "data" / "input" / "restaurant_sales_dirty.csv"

    if not file_path.exists():
        logger.error(f"❌ Arquivo não encontrado: {file_path}")    
        return None

    try:
        df = pd.read_csv(file_path, sep=",", engine="python", on_bad_lines="warn")
    except Exception as e:
        logger.error(f"⚠️ Erro ao ler o arquivo: {e}")
        return None


    df.columns = df.columns.str.lower()


    col_not_transform = ["order_id","customer_id"]
    
    

            
    logger.info(f"\n✅ Arquivo carregado com sucesso: {file_path.name}")
    logger.info(f"📊 Linhas: {len(df)}, Colunas: {len(df.columns)}\n")


    return df


if __name__ == "__main__":

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    
    df = extract_data()

    logger.info("Prévia dos dados (10 primeiras linhas):")
    logger.info(f"{df.head(10)}\n")

    logger.info("Prévia das últimas 10 linhas:")
    logger.info(f"{df.tail(10)}\n")