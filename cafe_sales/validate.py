import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def validate_data(df: pd.DataFrame) -> bool:
    
    logger.info("🔍 Iniciando validação inteligente dos dados...")

    required_cols = ["expected_total", "diff", "suspect_transaction"]
    for col in required_cols:
        if col not in df.columns:
            logger.warning(f"⚠️ Coluna ausente: {col}")
            return False