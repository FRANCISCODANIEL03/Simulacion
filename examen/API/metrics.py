from reduced_ds import red_ds
from divide_dataset import d_val_set, d_train_set
from prepare_ds import prepare_dataset
from sklearn.svm import SVC
from sklearn.metrics import f1_score, precision_score, recall_score

x_train_reduced, x_val_reduced = red_ds()
x_val, y_val = d_val_set()
x_train, y_train = d_train_set()
x_train_prep, x_val_prep, x_test_prep = prepare_dataset()

# SVM Large Margin Classification 
svm_clf = SVC(probability=True)
svm_clf.fit(x_train_reduced, y_train)

def pred_metrics():
    # Predecir un DataSet reducido
    y_pred = svm_clf.predict(x_val_reduced)

    f1score = f1_score(y_pred, y_val, average ="weighted")
    precision = precision_score(y_val, y_pred, average ="weighted")
    recall = recall_score(y_val, y_pred, average ="weighted")
    return f1score, precision, recall

#svm_clf_c = SVC(kernel = "linear", C=1)
#svm_clf_c.fit(x_train_prep, y_train)
#def pred_metrics2():
    #y_pred = svm_clf_c.predict(x_val_reduced)

    #f1score = f1_score(y_pred, y_val, average ="weighted")
    #precision = precision_score(y_val, y_pred, average ="weighted")
    #recall = recall_score(y_val, y_pred, average ="weighted")
    #return f1score, precision, recall

