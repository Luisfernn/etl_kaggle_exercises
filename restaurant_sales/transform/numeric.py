import pandas as pd
import logging

def numeric_transformation(df):
    df.loc[valid, "price"] = df.loc[valid, "price"].fillna(0)