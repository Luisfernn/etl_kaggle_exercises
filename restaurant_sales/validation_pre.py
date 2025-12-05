from extract import extract_data
import pandas as pd
import logging

def validation_data(df: pd.DataFrame) -> pd.DataFrame:

    valid = df["valid_line"] == True
    
    df["valid_line"] = df["order_total"] > 0.01

    return df