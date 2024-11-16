from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

# Transformador para codificar unicamente las columnas categoricas y devolver un DataFrame
class CustomOneHotEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._oh = OneHotEncoder(sparse_output = False)
        self._columns = None
    def fit(self, x, y = None):
        x_cat = x.select_dtypes(include = ['object'])
        self._columns = pd.get_dummies(x_cat).columns
        self._oh.fit(x_cat)
        return self
    def transform(self, x, y = None):
        x_copy = x.copy()
        x_cat = x_copy.select_dtypes(include = ['object'])
        x_num = x_copy.select_dtypes(exclude = ['object'])
        x_cat_oh = self._oh.transform(x_cat)
        x_cat_oh = pd.DataFrame(x_cat_oh, columns = self._columns, index = x_copy.index)
        x_copy.drop(list(x_cat), axis = 1, inplace = True)
        return x_copy.join(x_cat_oh)