import arff
import pandas as pd

def load_kdd_dataset(data_path):
    """Lectura de DataSet NSL-KDD."""
    with open(data_path, 'r') as train_set:
        dataset = arff.load(train_set)
    
    # Asegúrate de que 'dataset' tiene las claves esperadas
    if "attributes" not in dataset:
        raise KeyError("'attributes' no está presente en el dataset cargado.")
    if "data" not in dataset:
        raise KeyError("'data' no está presente en el dataset cargado.")
    
    # Convertir 'attributes' en una lista si es un generador
    attributes = [attr[0] for attr in list(dataset["attributes"])]
    
    # Crear el DataFrame usando los atributos como columnas
    return pd.DataFrame(dataset["data"], columns=attributes)
