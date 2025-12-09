import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def validation_post_data(df):

    assert df["price"].dtype in ["float64", "int64"], "price is not numeric after transformation"
    assert df["quantity"].dtype in ["int64"], "quantity not converted to integer"
    assert df["item"].notna().all(), "item has NaN after text cleaning"
    assert df["payment_method"].notna().all(), "payment_method has NaN after text cleaning"

    nan_counts = df.isna().sum()

    logger.info("Pós_validation: Contagem de NaN por colunas:")
    logger.info(f"\n{nan_counts}")

    return df