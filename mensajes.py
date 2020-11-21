
#modulo para mandar mensajes
from PyQt5 import  QtGui, QtWidgets

#mensaje para cerrar ventana
def cerrar_ventana(self,event):

    reply = QtWidgets.QMessageBox.question(self,
                             'Events - Cerrar Ventana',
                             "Realmente desea cerrar la aplicacion",
                             QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
    if reply == QtWidgets.QMessageBox.Yes:
        event.accept()
    else:
        event.ignore()
    return reply
#mensaje advertencia, exito, cualquiera de solo informar
def showMessage(titulo, texto):
    # instanciamos un QMessageBox
    msg = QtWidgets.QMessageBox()
    #le definimos su icono
    msg.setIcon(QtWidgets.QMessageBox.Information)
    # le damos titulo
    msg.setWindowTitle(titulo)
    # le damos texto
    msg.setText(texto)
    # lo personalizamos
    msg.setStyleSheet(
        "QMessageBox{background-color:black;}QMessageBox QLabel {color:white;}QMessageBox QPushButton{background-color: white;color:black}")
    msg.setFont(QtGui.QFont('Trebuchet MS', 12))
    #lo ejecutamos
    msg.exec_()
#mensaje para aceptar transaccion
def showdialog(titulo, text):
    # instanciamos un QMessageBox
    msg = QtWidgets.QMessageBox()
    # le definimos un icono
    msg.setIcon(QtWidgets.QMessageBox.Information)
    #le definimos su texto
    msg.setText(text)
    #le definimo su titulo
    msg.setWindowTitle(titulo)
    #definimos sus botones
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
    #lo personalizamos
    msg.setStyleSheet(
        "QMessageBox{background-color:black;}QMessageBox QLabel {color:white;}QMessageBox QPushButton{background-color: white;color:black}")
    msg.setFont(QtGui.QFont('Trebuchet MS', 12))
    #definimos su tamaño
    msg.setMinimumSize(200, 300)
    msg.setMaximumSize(200, 300)
    #guardamos la ejecución de este y los valores que elija el usuario segun la opcion que elija en una variable
    retval = msg.exec_()
    #retornamos la variable con los valores de respuesta
    return retval