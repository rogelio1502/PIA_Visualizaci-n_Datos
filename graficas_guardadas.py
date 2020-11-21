# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graficas_guardadas.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
#ui de las graficas guardadas

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_configuraciones_anteriores(object):
    def setupUi(self, configuraciones_anteriores):
        configuraciones_anteriores.setObjectName("configuraciones_anteriores")
        configuraciones_anteriores.resize(928, 473)
        configuraciones_anteriores.setStyleSheet("border: 1px solid #d0d0d0;\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);")
        self.tabla_graficas = QtWidgets.QTableWidget(configuraciones_anteriores)
        self.tabla_graficas.setGeometry(QtCore.QRect(30, 90, 871, 271))
        self.tabla_graficas.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Trebuchet MS\";\n"
"color: rgb(0, 0, 0);")
        self.tabla_graficas.setObjectName("tabla_graficas")
        self.tabla_graficas.setColumnCount(9)
        self.tabla_graficas.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_graficas.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_graficas.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_graficas.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_graficas.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_graficas.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_graficas.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_graficas.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_graficas.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabla_graficas.setHorizontalHeaderItem(8, item)
        self.titulo = QtWidgets.QLabel(configuraciones_anteriores)
        self.titulo.setGeometry(QtCore.QRect(100, 10, 751, 61))
        self.titulo.setStyleSheet("font: 75 16pt \"Trebuchet MS\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.titulo.setObjectName("titulo")
        self.btn_consultar = QtWidgets.QPushButton(configuraciones_anteriores)
        self.btn_consultar.setGeometry(QtCore.QRect(230, 390, 171, 51))
        self.btn_consultar.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Trebuchet MS\";\n"
"background-color: rgb(0, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.btn_consultar.setObjectName("btn_consultar")
        self.btn_eliminar = QtWidgets.QPushButton(configuraciones_anteriores)
        self.btn_eliminar.setGeometry(QtCore.QRect(520, 390, 171, 51))
        self.btn_eliminar.setStyleSheet("font: 75 12pt \"Trebuchet MS\";background-color: rgb(255, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"")
        self.btn_eliminar.setObjectName("btn_eliminar")

        self.retranslateUi(configuraciones_anteriores)
        QtCore.QMetaObject.connectSlotsByName(configuraciones_anteriores)

    def retranslateUi(self, configuraciones_anteriores):
        _translate = QtCore.QCoreApplication.translate
        configuraciones_anteriores.setWindowTitle(_translate("configuraciones_anteriores", "Configuraciones guardadas"))
        item = self.tabla_graficas.horizontalHeaderItem(0)
        item.setText(_translate("configuraciones_anteriores", "FECHA"))
        item = self.tabla_graficas.horizontalHeaderItem(1)
        item.setText(_translate("configuraciones_anteriores", "NOMBRE"))
        item = self.tabla_graficas.horizontalHeaderItem(2)
        item.setText(_translate("configuraciones_anteriores", "TIPO"))
        item = self.tabla_graficas.horizontalHeaderItem(3)
        item.setText(_translate("configuraciones_anteriores", "LIBRERIA"))
        item = self.tabla_graficas.horizontalHeaderItem(4)
        item.setText(_translate("configuraciones_anteriores", "ETIQUETA X"))
        item = self.tabla_graficas.horizontalHeaderItem(5)
        item.setText(_translate("configuraciones_anteriores", "VALORES X"))
        item = self.tabla_graficas.horizontalHeaderItem(6)
        item.setText(_translate("configuraciones_anteriores", "ETIQUETA Y"))
        item = self.tabla_graficas.horizontalHeaderItem(7)
        item.setText(_translate("configuraciones_anteriores", "VALORES Y"))
        item = self.tabla_graficas.horizontalHeaderItem(8)
        item.setText(_translate("configuraciones_anteriores", "COMENTARIOS"))
        self.titulo.setText(_translate("configuraciones_anteriores", "ELIJA UN REGISTRO PARA SU CONSULTA Y GENERACIÓN O PARA SU ELIMINACIÓN"))
        self.btn_consultar.setText(_translate("configuraciones_anteriores", "CONSULTAR"))
        self.btn_eliminar.setText(_translate("configuraciones_anteriores", "ELIMINAR"))
