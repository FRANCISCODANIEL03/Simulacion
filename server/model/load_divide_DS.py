from load_kdd_dataset import load_kdd_dataset
from train_val_test_split import train_val_test_split 
import pandas as pd 

df = load_kdd_dataset("/home/pako0311/Escritorio/Simulacion/datasets/datasets/NSL-KDD/KDDTrain+.arff")

#Division del DataSet en los diferentes subconjuntos
train_set, val_set, test_set = train_val_test_split(df)
