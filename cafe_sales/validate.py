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

    valid_rows = (
    df["price_per_unit"].notna()
    & df["quantity"].notna()
    & df["total_spent"].notna()
)        
 
    if df.loc[valid_rows, "expected_total"].isna().any():
    logger.warning("⚠️ expected_total está NaN em linhas onde deveria existir.")
    return False

    if df.loc[valid_rows, "diff"].isna().any():
        logger.warning("⚠️ diff está NaN em linhas onde deveria existir.")
        return False

    if df["suspect_transaction"].isna().any():
        logger.warning("⚠️ suspect_transaction contém NaN (não deveria).")
        return False    