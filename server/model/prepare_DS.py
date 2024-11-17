from data_frame_preparer import DataFramePreparer
from load_divide_DS import datasetGen, dsTrain, dsVal, dsTest

# instanciamos nuestro transformador personalizado
x_df, y_df = datasetGen()
x_train, y_train = dsTrain()
x_val, y_val = dsVal()
x_test, y_test = dsTest()

data_preparer = DataFramePreparer()

