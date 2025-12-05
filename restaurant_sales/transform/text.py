import pandas as pd
import logging

def text_transformation(df):
    df_valid = df["valid_line"] == True