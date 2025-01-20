from data_frame_preparer import DataFramePreparer
from load_divide_DS import datasetGen, dsTrain, dsVal, dsTest

# Instanciar el transformador personalizado y cargar los datos
data_preparer = DataFramePreparer()
x_df, y_df = datasetGen()
x_train, y_train = dsTrain()
x_val, y_val = dsVal()
x_test, y_test = dsTest()

# Ajustar el transformador solo una vez
data_preparer.fit(x_df)

def transform_dataset(dataset):
    """Transforma un dataset usando el preparador de datos."""
    return data_preparer.transform(dataset)

# Funciones para preparar datasets específicos
def dsPreparer():
    x_train_prep = transform_dataset(x_train)
    x_val_prep = transform_dataset(x_val)
    return x_train_prep, x_val_prep

def DSpreparer(dataSet):
    return transform_dataset(dataSet)
