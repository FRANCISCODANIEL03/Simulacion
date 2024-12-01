from sklearn.preprocessing import RobustScaler
from pandas import DataFrame
from read_csv import divide_DS_train, divide_DS_val, divide_DS_test

X_train, y_train = divide_DS_train()
X_val, y_val = divide_DS_val()
X_test, y_test = divide_DS_test()
