from sklearn.impute import SimpleImputer
from divide_dataset import d_train_set, d_val_set, d_test_set
import pandas as pd

x_train2, y_train = d_train_set()
x_val2, y_val = d_val_set()
x_test2, y_test = d_test_set()
