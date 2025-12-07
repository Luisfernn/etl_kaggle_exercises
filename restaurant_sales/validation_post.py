import pandas as pd
import logging


def validation_post(df):

    assert df["price"].dtype in ["float64", "int64"], "price is not numeric after transformation"