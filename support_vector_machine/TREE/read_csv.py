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
