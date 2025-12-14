import pandas as pd
import logging
from pandas.api.types import is_integer_dtype, is_numeric_dtype

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def validation_post_data(df, valid):

    assert is_numeric_dtype(df["price"]), \
        "price is not numeric after transformation"

    assert is_integer_dtype(df.loc[valid, "quantity"]), \
        "quantity not converted to integer"

    assert is_numeric_dtype(df.loc[valid, "order_total"]), \
        "order_total is not numeric after transformation"

    
    assert df.loc[valid, "item"].notna().all(), \
        "item has NaN in valid lines after text cleaning"

    assert df.loc[valid, "payment_method"].notna().all(), \
        "payment_method has NaN in valid lines after text cleaning"


    nan_counts = df.isna().sum()

    logger.info("Pós_validation: Contagem de NaN por colunas:")
    logger.info(f"\n{nan_counts}")

    return df