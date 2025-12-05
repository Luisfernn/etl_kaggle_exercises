import pandas as pd
import logging

def text_transformation(df):
    df_valid = df["valid_line"] == True

    df.loc[df["valid_line"], "item"] = df["item"].fillna("unknown")