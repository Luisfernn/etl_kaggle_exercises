import pandas as pd 

def transform_text(df: pd.DtaFrame, exclude_columns=None, transformations=Nome) -> pd.DtaFrame:

    if exclude_columns is None:
        exclude_columns = []

    if transformations is None:
        transformations = []

    text_columns = df.select_dtypes(include='object').columns 

    columns_to_transform = [col for col in text_columns if col not in exclude_columns]


if __name__ == "__main__":

    from pathlib import Path
    import pandas as pd

    file_path = Path(__file__)