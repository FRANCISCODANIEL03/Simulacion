from train_split import train_val_test_split
from load_arff import load_kdd_dataset

df = load_kdd_dataset('/home/pako0311/Escritorio/DATASET/Dry_Bean_Dataset.arff')

train_set, val_set, test_set = train_val_test_split(df)
