from train_split import train_val_test_split
import pandas as pd

df = pd.read_csv("/home/pako0311/Escritorio/Simulacion/datasetsSVM/Malware.csv")

train_set, val_set, test_set = train_val_test_split(df)
# Eliminar los atributos que contengan valores infinitos

def d_train_set():
    x_train = train_set.drop('URL_Type_obf_Type', axis=1)
    #X_train = x_train.drop("argPathRatio", axis = 1)
    y_train = train_set['URL_Type_obf_Type'].copy()
    return X_train, y_train

def d_val_set():
    x_val = val_set.drop('URL_Type_obf_Type', axis=1)
    X_val = x_val.drop("argPathRatio", axis = 1)
    y_val = val_set['URL_Type_obf_Type'].copy()
    return X_val, y_val

def d_test_set():
    x_test = test_set.drop('URL_Type_obf_Type', axis=1)
    X_test = x_test.drop("argPathRatio", axis = 1)
    y_test = test_set['URL_Type_obf_Type'].copy()
    return X_test, y_test