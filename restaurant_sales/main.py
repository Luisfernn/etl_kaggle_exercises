import logging
import pandas as pd
from pathlib import Path
from pipeline import run_pipeline
from load import load_data

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "data" / "input" / "restaurant_sales_dirty.csv"
OUTPUT_DIR = BASE_DIR / "data" / "output"
LOG_DIR = BASE_DIR / "data" / "logs"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "etl.log", mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    try:
        logger.info("🚀 Iniciando execução da pipeline...")

        df_raw = pd.read_csv(INPUT_FILE)
        df = run_pipeline(df_raw)

        if df is not None:
            logger.info("💾 Carregando dados no diretório de saída...")
            load_data(df, file_name="restaurant_sales_clean.csv") 
            logger.info("✅ Pipeline finalizada com sucesso!")
        else:
            logger.warning("⚠️ A pipeline retornou None. Nenhum dado foi carregado.")
    except Exception as e:
        logger.error(f"❌ Pipeline falhou: {e}", exc_info=True)