from parse_email import parse_email
from parse_email import parse_index

def create_prep_dataset(index_path, n_elements):
    x = []
    y = []
    indexes = parse_index(index_path, n_elements)
    for i in range(n_elements):
        print("\rParsing email: {0}".format(i+1), end = "")
        mail, label = parse_email(indexes[i])
        x.append(" ".join(mail['subject']) + " ".join(mail['body']))
        y.append(label)
    return x, y