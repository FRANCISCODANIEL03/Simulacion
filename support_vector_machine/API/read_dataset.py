import pandas as pd
import numpy as np

def read_ds():
    df = pd.read_csv("/home/pako0311/Escritorio/Simulacion/datasetsSVM/Malware.csv")

    df["URL_Type_obf_Type"].value_counts()
    return df