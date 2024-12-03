import pandas as pd
from funciones_aux import train_val_test_split, remove_labels

df = pd.read_csv('/home/pako0311/Escritorio/Simulacion/datasets/datasets/TotalFeatures-ISCXFlowMeter.csv')

# Copiamos el conjunto de datos y transformamos la variable 
# de salida a numérica para calcular correlaciones
X = df.copy()
X['calss'] = X['calss'].factorize()[0]

# Calculamos correlaciones
corr_matrix = X.corr()
corr_matrix["calss"].sort_values(ascending=False)

X.corr()

corr_matrix[corr_matrix["calss"] > 0.05]

# Dividimos el conjunto de datos
train_set, val_set, test_set = train_val_test_split(X)

def divide_DS_train():
    X_train, y_train = remove_labels(train_set, 'calss')
    return X_train, y_train
