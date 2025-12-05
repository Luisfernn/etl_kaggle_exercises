import pandas as pd
import logging

def text_transformation(df):
    valid = df["valid_line"] == True

    df.loc[df[valid], "item"] = df.loc[valid, "item"].fillna("unknown")