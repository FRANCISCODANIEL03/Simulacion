from train_split import train_val_test_split
import pandas as pd
import numpy as np

df = pd.read_csv("/home/pako0311/Escritorio/Simulacion/datasetsSVM/Phishing.csv")

train_set, val_set, test_set = train_val_test_split(df)

def d_train_set():
    x_train = train_set.drop('URL_Type_obf_Type', axis=1)
    y_train = train_set['URL_Type_obf_Type'].copy()
    return x_train, y_train

