import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def numeric_transformation(df, valid):
    
    etapa = None
    
    try:
        etapa = "Preenchendo com 0 linhas validas vazias em price"
        df.loc[valid, "price"] = df.loc[valid, "price"].fillna(0)

        etapa = "Preenchendo com 0 linhas validas vazias em price e transformando os dados da coluna em int"
        df.loc[valid, "quantity"] = df.loc[valid, "quantity"].fillna(0).astype(int)

        return df

    except Exception as e:
        logger.error(f"❌ Erro na etapa: {etapa}")
        raise