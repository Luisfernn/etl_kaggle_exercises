import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def validate_data(df: pd.DataFrame) -> bool:

    logger.info("🔍 Iniciando validação de integridade dos dados...")

    expected_cols = ["expected_total", "diff", "suspect_transaction"]
    for col in expected_cols:
        if col not in df.columns:
            logger.warning(f"⚠️ Coluna ausente: {col}")

        elif df[col],isna().any():
            logger.warning(f"⚠️ Valores ausentes em: {col}")
            missing_columns.append(col)

    if len(missing_columns) == 0:
        logger.info("✅ Validação concluída com sucesso.")
        return True
    else:
        logger.warning("⚠️ Validação encontrou problemas.")
        return False