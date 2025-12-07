from extract import extract_data
import pandas as pd
import logging

def validation_data(df: pd.DataFrame) -> pd.DataFrame:

    required_columns = {"item", "quantity", "payment_method", "valid_line"}
    missing = required_columns - set(df.collumns)
    assert len(missing) == =, f"Missing required columns: {missing}"

    valid = df["valid_line"] == True

    df["valid_line"] = df["order_total"] > 0.01

    return df, valid