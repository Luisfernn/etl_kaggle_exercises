from pathlib import Path
import pandas as pd
import logging


logger = logging.getLogger(__name__)
logger.propagate = False
logger.addHandler(logging.NullHandler())

def clean_text(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    text_columns = ['item', 'payment_method', 'location']

    for col in text_columns:

        df[col] = df[col].where(df[col].isna(), df[col].str.lower())

    df['item'] = df['item'].replace('unknown', pd.NA)
    df['item'] = df['item'].fillna('unknown_item')

    df['payment_method'] = df['payment_method'].replace(['unknown', 'error'], pd.NA)
    df['payment_method'] = df['payment_method'].fillna('unknown_payment')

    df['location'] = df['location'].replace('unknown', pd.NA)
    df['location'] = df['location'].fillna('unknown_location')

    logger.info("✅ Transformações de texto aplicadas:")
    for col in text_columns:
        logger.info(f"Coluna '{col}' - valores únicos: {df[col].unique()[:10]}")

    return df


if __name__ == "__main__":
    base_dir = Path(__file__).resolve().parent
    file_path = base_dir / "data" / "input" / "dirty_cafe_sales.csv"

    df = pd.read_csv(file_path)
    df_clean = clean_text(df)
    print(df_clean.head(10))