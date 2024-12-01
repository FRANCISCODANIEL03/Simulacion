from sklearn.tree import DecisionTreeClassifier
from read_csv import divide_DS_train, divide_DS_val, divide_DS_test
from escalar_ds import x_train_scaled, x_val_scaled
from funciones_aux import evaluate_result
from sklearn.metrics import confusion_matrix, recall_score, f1_score, precision_score

MAX_DEPTH = 20
X_train, y_train = divide_DS_train()
X_val, y_val = divide_DS_val()
X_test, y_test = divide_DS_test()
X_train_scaled = x_train_scaled()
X_val_scaled = x_val_scaled()
