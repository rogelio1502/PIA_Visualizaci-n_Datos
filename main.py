#archivo principal para la ejecucion del programa
#importamos las librerias necesarias
import sys
from PyQt5 import QtWidgets
from cover import Ui_Pantalla_Inicio_PIA
from mensajes import showdialog
from home_main import Home
import matplotlib.pyplot as plt
from conexion_base_datos import crear_base_datos

#nombre de la base de datos
db = "graficas"
#clase principal que arroja el pantallazo inicial
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        #instanciamos la ui de la pantalla principal
        self.ui=Ui_Pantalla_Inicio_PIA()
        #actualizamos el diseño de la ventana
        self.ui.setupUi(self)
        #damos conectividad a botones
        self.ui.btn_go.clicked.connect(self.abrir_generador)


    #metodo para abrir generador/capturador de los datos de la grafica
    def abrir_generador(self):
        self.close()
        #instanciamos la clase Home donde esta cargada la ui de la ventana del configurador
        self.home = Home()
        self.home.ui.btn_volver.clicked.connect(self.volver)

    #metodo para preguntar si desea volver y advertir que se borraran los datos
    def volver(self):

        _volver = showdialog("Advertencia", "Si Vuelve, los datos se perderán.")
        if _volver == 1024:
            try:
                plt.close()
            except:
                pass
            self.show()
            self.home.close()
            try:

                self.home.guardar.close()
            except:
                pass
            try:
                self.home.guardadas.close()
            except:
                pass



#condicion main para la correcta ejecucion del programa
if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    #crear base de datos si es que no la tenemos
    crear_base_datos(db)
    ventana = MyApp()
    ventana.show()
    app.setStyle("Windows")
    sys.exit(app.exec_())