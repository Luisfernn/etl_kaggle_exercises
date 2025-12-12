import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def text_transformation(df, valid):

    try:
        etapa = None
        
        etapa = "Preencher com unknown linhas válidas vázias da coluna item"
        df.loc[valid, "item"] = df.loc[valid, "item"].fillna("unknown")

        
        etapa = "Preencher com unknown linhas válidas vázias da coluna payment_method"
        df.loc[valid, "payment_method"] = df.loc[valid, "payment_method"].fillna("unknown")

        return df, valid

    except Exception as e:
        logger.error(f"❌ Erro na etapa: {etapa}")