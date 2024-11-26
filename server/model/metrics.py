from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics import accuracy_score
from create_prep_DS import create_prep_dataset

# Leer 15,000 correos elctrónicos 
x, y = create_prep_dataset("/home/pako0311/Escritorio/Simulacion/datasets/datasets/trec07p/full/index", 70000)

# Utilizamos 10000 correos para entrenar el algoritmo y 2000 para realizar pruebas 
x_train, y_train = x[:60000], y[:60000]
x_test, y_test = x[60000:], y[60000:]

vectorizer = CountVectorizer()
x_train = vectorizer.fit_transform(x_train)

clf = LogisticRegression()
clf.fit(x_train, y_train)
