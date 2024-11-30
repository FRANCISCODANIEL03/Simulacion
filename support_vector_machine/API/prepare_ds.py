from sklearn.impute import SimpleImputer
from divide_dataset import d_train_set, d_val_set, d_test_set
import pandas as pd

x_train2, y_train = d_train_set()
x_val2, y_val = d_val_set()
x_test2, y_test = d_test_set()

def prepare_dataset():
    # Eliminar los atributos que contegan valores infinitos 
    x_train = x_train2.drop("argPathRatio", axis=1)
    x_val = x_val2.drop("argPathRatio", axis=1)
    x_test = x_test2.drop("argPathRatio", axis=1)

    # Rellenar los atributos que contenan valores infinitos

    imputer = SimpleImputer(strategy='median')

    x_train_prep = imputer.fit_transform(x_train)
    x_val_prep = imputer.fit_transform(x_val)
    x_test_prep = imputer.fit_transform(x_test)

    # Transformar el DataFrame de pandas
    x_train_prep = pd.DataFrame(x_train_prep, columns = x_train.columns, index = y_train.index)
    x_val_prep = pd.DataFrame(x_val_prep, columns = x_val.columns, index = y_val.index)
    x_test_prep = pd.DataFrame(x_test_prep, columns = x_test.columns, index = y_test.index)

    return x_train_prep, x_val_prep, x_test_prep