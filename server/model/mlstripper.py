# En esta clase facilita el preprocesamiento de correos electrónicos que poseen código HTML
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.fed = []
    def handle_data (self,d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)
    
# Esta funcion se encarga de eliminar los tags HTML que se encuentren en el texto de correo electronico
def strip_tags(HTML):
    s = MLStripper()
    s.feed(HTML)
    return s.get_data()