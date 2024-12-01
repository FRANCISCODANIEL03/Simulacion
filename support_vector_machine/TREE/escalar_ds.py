from sklearn.preprocessing import RobustScaler
from pandas import DataFrame
from read_csv import divide_DS_train, divide_DS_val, divide_DS_test

X_train, y_train = divide_DS_train()
X_val, y_val = divide_DS_val()
X_test, y_test = divide_DS_test()

def x_train_scaled():
    scaler = RobustScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    # Transformación a un DataFrame de Pandas
    X_train_scaled = DataFrame(X_train_scaled, columns=X_train.columns, index=X_train.index)
    return X_train_scaled

def x_test_scaled():
    scaler2 = RobustScaler()
    X_test_scaled = scaler2.fit_transform(X_test)
    return X_test_scaled
