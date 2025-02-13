from reduced_ds import red_ds
from divide_dataset import d_val_set, d_train_set
from prepare_ds import prepare_dataset
from sklearn.svm import SVC
from sklearn.metrics import f1_score, precision_score, recall_score

x_train_reduced, x_val_reduced = red_ds()
x_val, y_val = d_val_set()
x_train, y_train = d_train_set()
x_train_prep, x_val_prep, x_test_prep = prepare_dataset()
