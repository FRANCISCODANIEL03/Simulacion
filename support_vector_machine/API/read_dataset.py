import pandas as pd
import numpy as np

def read_ds():
    df = pd.read_csv("/home/pako0311/Escritorio/Simulacion/datasetsSVM/Phishing.csv")

    df["URL_Type_obf_Type"].value_counts()
    # Comprobar si existen valores infinitos
    is_inf = df.isin([np.inf, -np.inf]).any()
    is_inf[is_inf]
    return df