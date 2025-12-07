import pandas as pd
import logging


def validation_post(df):

    assert df["price"].dtype in ["float64", "int64"], "price is not numeric after transformation"
    assert df["quantity"]dtype in ["int64"], "quantity not converted to integer"