from pathlib import Path
import pandas as pd

def extract_data(file_path: Path = None):

    if file_path is None:
        base_dir = Path(__file__).resolve().parent
        file_path = / "data" / "input" / "dirty_cafe_sales.csv"

     df = pd.read_csv(file_path)     

     print(f"\n✅ Arquivo carregado com sucesso: {file_path}")
     print(f"📊 Linhas: {len(df)}, Colunas: {len(df.columns)}\n")

     print("Prévia dos dados (10 primeiras linhas):")
     print(df.head(10), "\n")

     print("Prévia das últimas 10 linhas:")
     print(df.tail(10), "\n")

     return df

if __name__ == "__main__":
    extract_data()