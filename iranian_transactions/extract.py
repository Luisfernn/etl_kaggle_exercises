from pathlib import Path
import pandas as pd

import logging 

logger = logger.getLogger(__name__)
logger = addHandler(logging.NullHandler())
logger.propagate = False

def extract_data(file_path: Path = None):

    if file_path is None:
        base_dir = Path(__file__).resolve().parent
        file_path = base_dir / "data" / "input" / "iranian_transaction_dirty.csv"

    if not file_path.exists():
        logger.error(f"❌ Arquivo {iranian_transaction_dirty} não encontrado.")
        return None

    try:
        df = pd.read_csv(file_path, sep=",", engine="python", on_bad_lines="warn")
    except Exception as e:
        logger.error(f"⚠️ Erro ao ler o arquivo: {e}")
        return None


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