from extract import extract_data
from validation_pre import validation_pre_data
from transformation.text import text_transformation
from transformation.numeric import numeric_transformation
from validation_post import validation_post_data
from load import load_data

import pandas as pd
import logging

def pipeline(df: pd.DataFrame) -> pd.DataFrame:

    try:
        etapa = None

        logging.info("Iniciando pipeline...")

        etapa = "Extração"
        logging.info("Iniciando extração de dados")
        df = extract_data(df)

        etapa = "Pré-validção"
        logging.info("Iniciando pré-validação...")
        df = validation_pre_data(df, valid)

        etapa = "Transformações de texto"
        logging.info("Iniciando transformações de texto...")
        df = text_transformation(df, valid)

        etapa = "Transformações numéricas"
        logging.info("Iniciando transformações numéricas...")
        df = numeric_transformation(df, valid)

        etapa = "Pós-validação"
        logging.info("Iniciando pós-validação...")
        df = validation_post_data(df, valid)

        return df

    except Exception as e:
        logging.error(f"❌ Erro na execução da etapa: {e}")
        raise
