import pandas as pd
import logging

def text_transformation(df):
    df_valid = df["valid_line"] == True

    for col in df:
        if col == df_valid:
            df["item"] = df["item"].fillna("unknown")