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


    if file_path.exists() and not overwrite:
        logger.error(f"❌ Arquivo já existe e overwrite=False: {file_path}")
        return None


    try:
        df.to_csv(file_path, index=False)
        logger.info(f"📁 Arquivo salvo com sucesso: {file_path}")
    except Exception as e:
        logger.error(f"⚠️ Erro ao salvar arquivo: {e}")
        return None

    return file_path
