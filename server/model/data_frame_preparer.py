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
