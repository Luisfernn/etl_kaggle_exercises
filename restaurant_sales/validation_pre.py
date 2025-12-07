from extract import extract_data
import pandas as pd
import logging

def validation_pre_data(df: pd.DataFrame) -> pd.DataFrame:

    required_columns = {"item", "quantity", "payment_method", "valid_line"}
    missing = required_columns - set(df.collumns)
    assert len(missing) == =, f"Missing required columns: {missing}"


    assert not df.empty, "DataFrame is empty after extract"


    if df.duplicated().any():
    logging.warning("There's duplicate lines in df.")


    valid = df["valid_line"] == True

    df["valid_line"] = df["order_total"] > 0.01


    numeric_cols = ["price", "quantity"]

    for col in numeric_cols:
        invalid = pd.to_numeric(df[col], errors="coerce").isna().sum()
        logger.warning(f"❗ Valores inválidos em '{col}': {invalid}")


    nan_counts = df.isna().sum

    logging.info("Pré_validation: Contagem de NaN por colunas:")
    logging.info(f"\n{nan_counts}")

    return df, valid