import logging
from pathlib import Path
from cafe_sales.pipeline import run_pipeline
from cafe_sales.load import load_data

BASE_DIR = Path(__file__).resolve().parent
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
        df = run_pipeline()
        if df is not None:
            logger.info("💾 Carregando dados no diretório de saída...")
            load_data(df, file_name="restaurant_sales_clean.csv") 
            logger.info("✅ Pipeline finalizada com sucesso!")
        else:
            logger.warning("⚠️ A pipeline retornou None. Nenhum dado foi carregado.")
    except Exception as e:
        logger.error(f"❌ Pipeline falhou: {e}", exc_info=True)