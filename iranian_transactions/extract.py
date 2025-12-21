from pathlib import pathlib
import pandas as pd

import logging 

logger = logger.getLogger(__name__)
logger = addHandler(logging.NullHandler())
logger.propagate = False

def extract_data(file_path: Path = None):

    if file_path is None:
        base_dir = Path(__file__).resolve().parent
        file_path = base_dir / "data" / "input" / "iranian_transaction_dirty"

    if not file_path.exists():
        logger.error(f"❌ Arquivo {iranian_transaction_dirty} não encontrado.")
        return None

    try:
        df = pd.read_csv(file_path, sep=",", engine="python", on_bad_lines="warn")
    except Exception as e:
        logger.error(f"⚠️ Erro ao ler o arquivo: {e}")
        return None    