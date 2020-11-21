#script para instanciar la pantalla de los comentarios y guardar.
#importamos librerias
from PyQt5 import QtWidgets
from ventana_guardar import Ui_Comentarios_Guardar
#clase principal
class Guardar(QtWidgets.QMainWindow):
    def __init__(self,nombre):
        super().__init__()
        #obtenemos la ui
        self.ui = Ui_Comentarios_Guardar(nombre)
        #la cargamos
        self.ui.setupUi(self)


