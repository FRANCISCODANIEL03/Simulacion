from data_frame_preparer import DataFramePreparer
from load_divide_DS import datasetGen, dsTrain, dsVal, dsTest

# instanciamos nuestro transformador personalizado
x_df, y_df = datasetGen()
x_train, y_train = dsTrain()
x_val, y_val = dsVal()
x_test, y_test = dsTest()

data_preparer = DataFramePreparer()

def dsPreparer():
    # Hacer el fit con el DataSet General para que adquiera todos los valores posibles 
    data_preparer.fit(x_df)

    # Transformar el DataSet de entrenamiento
    x_train_prep = data_preparer.transform(x_train)

    # Transformar el DataSet de validacion 
    x_val_prep = data_preparer.transform(x_val)
    return x_train_prep, x_val_prep

def DSpreparer(dataSet):
    x_prep = data_preparer.transform(dataSet)
    return x_prep

