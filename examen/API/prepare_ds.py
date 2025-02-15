from sklearn.impute import SimpleImputer
from divide_dataset import d_train_set, d_val_set, d_test_set
import pandas as pd

x_train, y_train = d_train_set()
x_val, y_val = d_val_set()
x_test, y_test = d_test_set()

def prepare_dataset():
    # Rellenar los atributos que contenan valores infinitos

    imputer = SimpleImputer(strategy='median')

    x_train_prep = imputer.fit_transform(x_train)
    x_val_prep = imputer.fit_transform(x_val)
    x_test_prep = imputer.fit_transform(x_test)

    # Transformar el DataFrame de pandas
    x_train_prep2 = pd.DataFrame(x_train_prep, columns = x_train.columns, index = y_train.index)
    x_val_prep2 = pd.DataFrame(x_val_prep, columns = x_val.columns, index = y_val.index)
    x_test_prep2 = pd.DataFrame(x_test_prep, columns = x_test.columns, index = y_test.index)

    return x_train_prep2, x_val_prep2, x_test_prep2