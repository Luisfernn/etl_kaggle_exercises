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
        df = extract(df)

        etapa = "Pré-validção"
        logging.info("Iniciando pré-validação...")
        df = validation_pre_data(df, valid)
