import pandas as pd
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def validate_data(df: pd.DataFrame) -> bool:

    logger.info("🔍 Iniciando validação de integridade dos dados...")

    expected_cols = ["expected_total", "diff", "suspect_transiction"]
    for col in expected_cols:
        if col not in df.columns:
            logger.warning(f"⚠️ Coluna ausente: {col}")

    numeric_cols = ["total_spent", "price_per_unit" "quantity"] 
    for col in numeric_cols:
        if df[col].isna().any():
            logger.waring(f"⚠️ Valores ausentes em {col}")

    inconsistents = (df["expected_total"] - (df["price_per_unit"] * df["quantity"])).abs() > 0.01
    if inconsistents.any():
        logger.waring(f"⚠️ {inconsistents.sum()} inconsistências detectadas entre o esperado e o calculado.")

    logger.info("✅ Validação concluída com sucesso.")    
    return df