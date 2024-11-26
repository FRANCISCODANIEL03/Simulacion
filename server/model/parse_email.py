import os
from parser import Parser

DATASET_PATH = "/home/pako0311/Escritorio/Simulacion/datasets/datasets/trec07p"

def parse_index(path_to_index, n_elements):
    ret_indexes = []
    index = open(path_to_index).readlines()
    for i in range(n_elements):
        mail = index[i].split(" ../")
        label = mail[0]
        path = mail[1][:-1]
        ret_indexes.append({
            "label":label,
            "email_path":os.path.join(DATASET_PATH, path)
        })
    return ret_indexes
