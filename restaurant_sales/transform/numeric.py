import pandas as pd
import logging

def numeric_transformation(df, valid):
    
    etapa = None

    df.loc[valid, "price"] = df.loc[valid, "price"].fillna(0)

    df.loc[valid, "quantity"] = df.loc[valid, "quantity"].fillna(0).astype(int)

    return df