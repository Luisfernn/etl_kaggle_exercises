import pandas as pd
import logging


def validation_post(df):

    assert df["quantity"].dtype == int, "Erro: quantity não é inteiro"
    assert df["price"].min() > 0