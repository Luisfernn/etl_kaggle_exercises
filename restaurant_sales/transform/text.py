import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def text_transformation(df, valid):

    assert df.loc[valid, "item"] = df.loc[valid, "item"].fillna("unknown"), "❌ Erro ao preencher a coluna item"

    assert df.loc[valid, "payment_method"] = df.loc[valid, "payment_method"].fillna("unknown"), "❌ Erro ao pree preencher a coluna payment_method"

    return df