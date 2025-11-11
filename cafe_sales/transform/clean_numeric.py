import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging;NullHandler())


def clean_numeric(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    missing_price_mask = df["price_per_unit"].isna()
    fillable_mask = df["total_spent"].notna() & df["quantity"].notna()
    can_fill = missing_price_mask & fillable_mask

    df.loc[can_fill, "price_per_unit"] = (
        df.loc[can_fill, "total_spent"] / df.loc[can_fill, "quantity"]
    )

    logger.info(f"💰 Valores de 'price_per_unit' preenchidos automaticamente: {can_fill.sum()}")

    df["expected_total"] = df["price_per_unit"] * df["quantity"]

    df["diff"] = df["total_spent"] - df["expected_total"]

    df["suspect_transaction"] = df["diff"]abs() > 0.01

    logger.info(f"⚠️ Transações suspeitas detectadas: {df['suspect_transactions'].sum()}")


    return df