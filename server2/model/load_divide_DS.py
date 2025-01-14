from load_kdd_dataset import load_kdd_dataset
from train_val_test_split import train_val_test_split 

df = load_kdd_dataset("/home/pako0311/Escritorio/Simulacion/server2/model/Rice_MSC_Dataset.arff")

#Division del DataSet en los diferentes subconjuntos
train_set, val_set, test_set = train_val_test_split(df)

def datasetGen():
    # DataSet general 
    x_df = df.drop("CLASS", axis = 1)
    y_df = df["CLASS"].copy()
    return x_df, y_df

def dsTrain():
    # DataSet de entrenamiento 
    x_train = train_set.drop("CLASS", axis = 1)
    y_train = train_set["CLASS"].copy()
    return x_train, y_train

def dsVal():
    # DataSet de validacion
    x_val = val_set.drop("CLASS", axis = 1)
    y_val = val_set["CLASS"].copy()
    return x_val, y_val

def dsTest():
    # DataSet de test
    x_test = test_set.drop("CLASS", axis = 1)
    y_test = test_set["CLASS"].copy()
    return x_test, y_test