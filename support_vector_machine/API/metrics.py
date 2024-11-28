from reduced_ds import red_ds
from divide_dataset import d_val_set, d_train_set
from prepare_ds import prepare_dataset
from sklearn.svm import SVC
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score

x_train_reduced, x_val_reduced = red_ds()
x_val, y_val = d_val_set()
x_train, y_train = d_train_set()
x_train_prep, x_val_prep, x_test_prep = prepare_dataset()

# SVM Large Margin Classification 
svm_clf = SVC(kernel = 'linear', C = 50)
svm_clf.fit(x_train_reduced, y_train)
