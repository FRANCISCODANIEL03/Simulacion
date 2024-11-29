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


polynomial_svm_clf = Pipeline([
    ('poly_features', PolynomialFeatures(degree=3)),
    ('scaler', StandardScaler()),
    ('svm_clf', LinearSVC(C=20, loss='hinge', random_state = 42, max_iter = 100000))
])

polynomial_svm_clf.fit(x_train_reduced, y_train_num)

def pred_reduced_f1s():
    y_pred = polynomial_svm_clf.predict(x_val_reduced)
    f1score =  f1_score(y_pred, y_val_num)
    return f1score
