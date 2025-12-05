import pandas as pd
import logging

def text_transformation(df):
    valid = df["valid_line"] == True

    df.loc[valid, "item"] = df.loc[valid, "item"].fillna("unknown")

    df.loc[valid, "payment method"] = df.loc[valid, "payment method"].fillna("unknown")

    return df