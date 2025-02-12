from train_split import train_val_test_split
from load_arff import load_kdd_dataset

df = load_kdd_dataset('/home/pako0311/Escritorio/DATASET/Dry_Bean_Dataset.arff')

train_set, val_set, test_set = train_val_test_split(df)

def d_train_set():
    x_train = train_set.drop('Class', axis=1)
    y_train = train_set['Class'].copy()
    return x_train, y_train

def d_val_set():
    x_val = val_set.drop('Class', axis=1)
    y_val = val_set['Class'].copy()
    return x_val, y_val
