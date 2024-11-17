from prepare_DS import dsPreparer, DSpreparer
from load_divide_DS import dsTrain, dsTest, dsVal
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression

# Entrenar el algoritmo basado en Regresión Logistica 
x_val, y_val = dsVal()
x_test, y_test = dsTest()
x_train, y_train = dsTrain()
x_train_prep, x_val_prep = dsPreparer()

clf = LogisticRegression(max_iter = 5000)  
clf.fit(x_train_prep, y_train)

