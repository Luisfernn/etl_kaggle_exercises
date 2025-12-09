from extract import extract_data
from validation_pre import validation_pre_data
from transformation.text import text_transformation
from transformation.numeric import numeric_transformation
from validation_post import validation_post_data
from load import load_data

import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def run_pipeline(df: pd.DataFrame) -> pd.DataFrame:

    try:
        etapa = None

        logger.info("Iniciando pipeline...")

        etapa = "Extração"
        logger.info("📄 Iniciando extração de dados")
        df = extract_data(df)

        etapa = "Pré-validação"
        logger.info("🔍 Iniciando pré-validação...")
        df, valid = validation_pre_data(df)

        etapa = "Transformações de texto"
        logger.info("✏️ Iniciando transformações de texto...")
        df = text_transformation(df, valid)

        etapa = "Transformações numéricas"
        logger.info("🔢 Iniciando transformações numéricas...")
        df = numeric_transformation(df, valid)

        etapa = "Pós-validação"
        logger.info("🔍✔️ Iniciando pós-validação...")
        df = validation_post_data(df, valid)

        return df

    except Exception as e:
        logger.error(f"❌ Erro na execução da etapa: {e}")
        raise