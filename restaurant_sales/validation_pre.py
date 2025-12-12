from extract import extract_data
import pandas as pd
import logging

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

def validation_pre_data(df: pd.DataFrame) -> pd.DataFrame:

    required_columns = {
        "order_id",
        "customer_id",
        "item",
        "quantity",
        "price",
        "payment_method",
        "order_date",
        "order_total"
    }
    missing = required_columns - set(df.columns)
    assert len(missing) == 0, f"Missing required columns: {missing}"


    assert not df.empty, "DataFrame is empty after extract"


    if df.duplicated().any():
        logging.warning("There's duplicate lines in df.")


    df["valid_line"] = df["order_total"] > 0.01
    valid = df["valid_line"] == True


    numeric_cols = ["price", "quantity", "order_total"]

    for col in numeric_cols:
        invalid = pd.to_numeric(df[col], errors="coerce").isna().sum()
        logger.warning(f"❗ Valores inválidos em '{col}': {invalid}")


    invalid_dates = pd.to_datetime(df["order_date"], errors="coerce").isna().sum() 
    logger.warning(f"❗ Datas inválidas: {invalid_dates}")   


    nan_counts = df.isna().sum()

    logging.info("Pré_validation: Contagem de NaN por colunas:")
    logging.info(f"\n{nan_counts}")

    return df, valid