import pandas as pd
import logging

def text_transformation(df, valid):

    df.loc[valid, "item"] = df.loc[valid, "item"].fillna("unknown")

    df.loc[valid, "payment_method"] = df.loc[valid, "payment_method"].fillna("unknown")

    return df