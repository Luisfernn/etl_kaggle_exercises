import logging 
from pathlib import Path
import pandas as pd

from cafe_sales.extract import  extract_data
from cafe_sales.clean_text import clean_text
from cafe_sales.clean_numeric import clean_numeric
from cafe_sales.validate import validate_data

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(OUTPUT_DIR / "etl.log", mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


def run_pipeline():
    try:
        logger.info("🚀 Iniciando pipeline ETL...")

        df = extract_data(DATA_DIR / "dirty_cafe_sales.csv")
        logger.info(f"📦 Dados extraídos: {len(df)} linhas.")

        df = clean_text(df)
        logger.info("🧹 Limpeza de texto concluída.")

        df = clean_numeric(df)
        logger.info("📊 Limpeza numérica concluída.")

        is_valid = validate_data(df)
        if not is_valid:
            logger.warning("⚠️ Dados inválidos detectados. Salvamento cancelado.")
            return


        output_file = OUTPUT_DIR / "clean_sales.csv"
        df.to_csv(output_file, index=False)
        logger.info(f"✅ Dados salvos com sucesso em: {output_file}")


    except Exception as e:
        logger.exception(f"❌ Erro inesperado na execução do pipeline {e}")  

if __name__ == "__main__":
    run_pipeline()