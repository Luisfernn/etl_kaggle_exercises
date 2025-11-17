import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def clean_numeric(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df["price_per_unit"] = pd.to_numeric(df["price_per_unit"], errors="coerce")
    df["total_spent"] = pd.to_numeric(df["total_spent"], errors="coerce")
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

    missing_price_mask = df["price_per_unit"].isna()
    fillable_mask = df["total_spent"].notna() & df["quantity"].notna()
    can_fill = missing_price_mask & fillable_mask

    df.loc[can_fill, "price_per_unit"] = (
        df.loc[can_fill, "total_spent"] / df.loc[can_fill, "quantity"]
    )

    df["expected_total"] = df["price_per_unit"] * df["quantity"]

    df["diff"] = df["total_spent"] - df["expected_total"]

    df["suspect_transaction"] = df["diff"].abs() > 0.01

    logger.info(f"⚠️ Transações suspeitas detectadas: {df['suspect_transaction'].sum()}")

    return df