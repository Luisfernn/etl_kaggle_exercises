import logging 
from pathlib import Path

from cafe_sales.extract import  extract_data
from cafe_sales.transform.clean_text import clean_text
from cafe_sales.transform.clean_numeric import clean_numeric
from cafe_sales.validate import validate_data

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def run_pipeline():
    try:
        logger.info("🚀 Iniciando pipeline ETL...")

        df = extract_data(DATA_DIR / "input" / "dirty_cafe_sales.csv")
        logger.info(f"📦 Dados extraídos: {len(df)} linhas.")

        df = clean_text(df)
        logger.info("🧹 Limpeza de texto concluída.")

        df = clean_numeric(df)
        logger.info("📊 Limpeza numérica concluída.")

        is_valid = validate_data(df)
        if not is_valid:
            logger.warning("⚠️ Dados inválidos detectados. Salvamento cancelado.")
            return

        return df    

    except Exception as e:
        logger.exception(f"❌ Erro inesperado na execução do pipeline {e}")  

if __name__ == "__main__":
    run_pipeline()