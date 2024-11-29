from divide_dataset import d_train_set, d_val_set
from reduced_ds import red_ds
from sklearn.svm import LinearSVC
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score

x_train, y_train = d_train_set()
x_val, y_val = d_val_set()
x_train_reduced, x_val_reduced = red_ds()

# Para representar el limite de decision de tiene que pasar la variable objetivo a numerica 
y_train_num = y_train.factorize()[0]
y_val_num = y_val.factorize()[0]

