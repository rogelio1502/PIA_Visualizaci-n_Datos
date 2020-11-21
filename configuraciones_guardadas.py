#importamos las librerias necesarias
from PyQt5 import QtWidgets,QtCore
from graficas_guardadas import Ui_configuraciones_anteriores
from conexion_base_datos import conectar,_cursor,desconectar,consultar
#nombre de la base de datos
bd = "graficas"
#clase principal de la pantalla donde se desplegran las configuraciobes
class Configuracion(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_configuraciones_anteriores()
        self.ui.setupUi(self)
        #llenamos la tabla
        self.fillTable()
    #metodo con el que borramos el contenido de la tabla
    def borrar_contenido(self):
        for i in reversed(range(self.ui.tabla_graficas.rowCount())):
            # por cada iteración, borramos la fila con indice del iterador
            self.ui.tabla_graficas.removeRow(i)
    #metodo para llenar la tabla
    def fillTable(self):
        self.borrar_contenido()
        conexion = conectar(bd)
        cursor = _cursor(conexion)
        lista = consultar(cursor)
        desconectar(conexion)

        for i in lista:
            print(i)
        for i in lista:
            # guardamos en una variable la posición de la fila en base a las filas
            rowPosition = self.ui.tabla_graficas.rowCount()
            # insertamos una fila en base a la variable anterior
            self.ui.tabla_graficas.insertRow(rowPosition)
            # obtenemos el numero de columnas
            numCols = self.ui.tabla_graficas.columnCount()
            # obtenemos el numero de filas
            numRows = self.ui.tabla_graficas.rowCount()
            # definimos el numero de filas
            self.ui.tabla_graficas.setRowCount(numRows)
            # definimos el numero de columnas
            self.ui.tabla_graficas.setColumnCount(numCols)
            # definimos una variable contadora
            c = 0
            # recorremos cada valor del elemento actual
            for y in i:
                #si son estos valores se convierten a combobox
                if c == 5 or c == 7:

                    cb = QtWidgets.QComboBox()

                    cb.setStyleSheet("QListView{background-color: gray;color:white;border: 1px solid #d0d0d0;}"
                        "QComboBox {background-color: gray;color:white;border: 1px solid #d0d0d0;}")
                    x = ""
                    for z in y:
                        if z == "|":
                            cb.addItem(x)
                            x = ""
                        else:

                            x = x + z



                    self.ui.tabla_graficas.setCellWidget(numRows - 1, c, cb)

                    c = c + 1
                else:
                    self.ui.tabla_graficas.setItem(numRows - 1, c, QtWidgets.QTableWidgetItem(str(y)))
                    flags = QtCore.Qt.ItemIsSelectable
                    self.ui.tabla_graficas.item(numRows - 1, c).setFlags(flags)
                    c = c +1

        #ordenamos la tabla en base a su fecha
        self.ui.tabla_graficas.sortItems(0, QtCore.Qt.DescendingOrder)








