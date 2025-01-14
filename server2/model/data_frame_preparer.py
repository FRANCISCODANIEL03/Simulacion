from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.compose import ColumnTransformer
from custom_one_hot_encoder import CustomOneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import RobustScaler
import pandas as pd
import numpy as np

# Construccion de un pipeline para los atributos numericos
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy = "median")),
    ('rbst_scaler', RobustScaler())
])

# Transformador que prepara todo el DataSet 
class DataFramePreparer(BaseEstimator, TransformerMixin):
    def __init__(self):
        self._full_pipeline = None
        self._columns = None
    def fit(self, x, y = None):
        num_attribs = list(x.select_dtypes(exclude = ['object']))
        cat_attribs = list(x.select_dtypes(include = ['object']))
        self._full_pipeline = ColumnTransformer([
            ("num", num_pipeline, num_attribs),
            ("cat", CustomOneHotEncoder(), cat_attribs),
        ])
        self._full_pipeline.fit(x)
        self._columns = pd.get_dummies(x).columns
        return self
    def transform(self, x, y = None):
        x_copy = x.copy()
        x_prep = self._full_pipeline.transform(x_copy)
        return pd.DataFrame(x_prep, columns = self._columns, index = x_copy.index)