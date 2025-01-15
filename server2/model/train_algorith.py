from prepare_DS import dsPreparer, DSpreparer
from load_divide_DS import dsTrain, dsTest, dsVal
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.linear_model import LogisticRegression

# Variables globales inicializadas como None
clf = None
x_test, y_test = None, None
x_val, y_val = None, None
x_val_prep = None

def initialize_model():
    global clf, x_test, y_test, x_val, y_val, x_val_prep
    # Cargar datos
    x_val, y_val = dsVal()
    x_test, y_test = dsTest()
    x_train, y_train = dsTrain()
    x_train_prep, x_val_prep = dsPreparer()

    # Entrenar modelo
    clf = LogisticRegression(max_iter=5000)
    clf.fit(x_train_prep, y_train)

def predict():
    global clf, x_test, y_test, x_val, y_val, x_val_prep

    # Asegurar que el modelo esté inicializado
    if clf is None:
        initialize_model()

    # Preparar los datos de prueba
    x_test_prep = DSpreparer(x_test)
    y_pred = clf.predict(x_test_prep)

    y_predR = clf.predict(x_val_prep)

    # Calcular métricas
    f1score = f1_score(y_test, y_pred, average="macro")
    recall = recall_score(y_val, y_predR, average="macro")
    precision = precision_score(y_val, y_predR, average="macro")
    return f1score, precision, recall
