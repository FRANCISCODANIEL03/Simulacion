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

# Modelo entrenado con el conjunto de datos sin escalar
clf_tree = DecisionTreeClassifier(max_depth=MAX_DEPTH, random_state=42)
clf_tree.fit(X_train, y_train)

# Modelo entrenado con el conjunto de datos escalado
clf_tree_scaled = DecisionTreeClassifier(max_depth=MAX_DEPTH, random_state=42)
clf_tree_scaled.fit(X_train_scaled, y_train)

def pred_escalar():
    # Predecimos con el conjunto de datos de entrenamiento
    y_train_pred = clf_tree.predict(X_train)
    y_train_prep_pred = clf_tree_scaled.predict(X_train_scaled)

    # Comparamos resultados entre escalado y sin escalar
    res1 , res2 = evaluate_result(y_train_pred, y_train, y_train_prep_pred, y_train, f1_score)
    return res1, res2


def pred_sin_escalar():
    # Predecimos con el conjunto de datos de validación
    y_pred = clf_tree.predict(X_val)
    y_prep_pred = clf_tree_scaled.predict(X_val_scaled)
    # Comparamos resultados entre escalado y sin escalar
    res1, res2 = evaluate_result(y_pred, y_val, y_prep_pred, y_val, f1_score)
    return res1, res2


