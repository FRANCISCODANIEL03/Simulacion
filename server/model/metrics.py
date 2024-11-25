from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics import accuracy_score
from create_prep_DS import create_prep_dataset

# Leer 15,000 correos elctrónicos 
x, y = create_prep_dataset("/home/pako0311/Escritorio/Simulacion/datasets/datasets/trec07p/full/index", 70000)
