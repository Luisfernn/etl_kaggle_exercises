from __future__ import annotations
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def validate_transactions(df: pd.DataFrame) -> pd.DataFrame:

    original_count = len(df)

    cleaned_total_spent = (
        df["total_spent"]
        .astype(str)
        .str.strip()
        .str.lower()
        .replace({"error": None, "unknown": None})
    )

    numeric_total = pd.to_numeric(cleaned_total_spent, errors="coerce")

    invalid_mask = numeric_total.isna() | (numeric_total <= 0)

    removed_count = invalid_mask.sum()
    kept_count = original_count - removed_count

    if removed_count > 0:
        logger.info(f"🚫 Transações removidas por falta de pagamento: {removed_count}")

    logger.info(f"✅ Transações mantidas: {kept_count}") 

    return df[~invalid_mask].copy()