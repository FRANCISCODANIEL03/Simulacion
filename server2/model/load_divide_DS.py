from load_kdd_dataset import load_kdd_dataset
from train_val_test_split import train_val_test_split

df = load_kdd_dataset("Dry_Bean_Dataset.arff")

# División del DataSet en los diferentes subconjuntos
train_set, val_set, test_set = train_val_test_split(df)

# Generar conjuntos `x` e `y` una vez
x_df, y_df = train_set.drop("Class", axis=1), train_set["Class"].copy()
x_train, y_train = train_set.drop("Class", axis=1), train_set["Class"].copy()
x_val, y_val = val_set.drop("Class", axis=1), val_set["Class"].copy()
x_test, y_test = test_set.drop("Class", axis=1), test_set["Class"].copy()

# Funciones que simplemente retornan los valores globales
def datasetGen():
    return x_df, y_df

def dsTrain():
    return x_train, y_train

def dsVal():
    return x_val, y_val

def dsTest():
    return x_test, y_test
