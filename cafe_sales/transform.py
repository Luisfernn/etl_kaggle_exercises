import pandas as pd 

def transform_data():

    print("🔧 Transformando data...")

    df = df.drop_duplicates()

    df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)