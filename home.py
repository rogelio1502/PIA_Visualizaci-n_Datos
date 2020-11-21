# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generación_gráficas.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#ui de home/generador de graficas
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_pantalla_visualizador_graficas(object):
    def setupUi(self, pantalla_visualizador_graficas):
        pantalla_visualizador_graficas.setObjectName("pantalla_visualizador_graficas")
        pantalla_visualizador_graficas.resize(1043, 900)
        pantalla_visualizador_graficas.setMinimumSize(QtCore.QSize(1043, 900))
        pantalla_visualizador_graficas.setMaximumSize(QtCore.QSize(2000, 900))
        pantalla_visualizador_graficas.setStyleSheet("background-color: rgb(0, 0, 0);color:white;")
        self.centralwidget = QtWidgets.QWidget(pantalla_visualizador_graficas)
        self.centralwidget.setObjectName("centralwidget")

        """
        
        Label fondo
        
        """
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 50, 951, 811))
        self.label.setStyleSheet("border: 1px solid #d0d0d0;\n"
"")
        self.label.setObjectName("label")


        """
        
        Label titulo principal
        
        """
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(170, 70, 709, 80))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_lbl_main = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_lbl_main.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_lbl_main.setObjectName("gridLayout_lbl_main")
        self.lbl_introduzca = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.lbl_introduzca.setStyleSheet("font: 75 20pt \"Trebuchet MS\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.lbl_introduzca.setObjectName("lbl_introduzca")
        self.gridLayout_lbl_main.addWidget(self.lbl_introduzca, 0, 0, 1, 1)


        """
        
        Datos gráfica
        
        """
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(70, 160, 369, 561))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_datos_grafica = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_datos_grafica.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_datos_grafica.setObjectName("gridLayout_datos_grafica")
        """"
                                
                                Tipo
                                
        """
        self.lbl_tipo = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_tipo.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 12pt \"Trebuchet MS\";")
        self.lbl_tipo.setObjectName("lbl_tipo")
        self.gridLayout_datos_grafica.addWidget(self.lbl_tipo, 1, 0, 1, 1)

        self.rb_pie = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.rb_pie.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rb_pie.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "font: 75 12pt \"Trebuchet MS\";")
        self.rb_pie.setObjectName("rb_pie")
        self.gridLayout_datos_grafica.addWidget(self.rb_pie, 4, 0, 1, 1)

        self.rb_barra = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.rb_barra.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rb_barra.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 12pt \"Trebuchet MS\";")
        self.rb_barra.setObjectName("rb_barra")
        self.gridLayout_datos_grafica.addWidget(self.rb_barra, 2, 0, 1, 1)

        self.rb_linea = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.rb_linea.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rb_linea.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "font: 75 12pt \"Trebuchet MS\";")
        self.rb_linea.setObjectName("rb_linea")
        self.gridLayout_datos_grafica.addWidget(self.rb_linea, 3, 0, 1, 1)
        """
        
                                Libreria
        
        """

        self.lbl_libreria = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_libreria.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "font: 75 12pt \"Trebuchet MS\";")
        self.lbl_libreria.setObjectName("lbl_libreria")
        self.gridLayout_datos_grafica.addWidget(self.lbl_libreria, 5, 0, 1, 1)

        self.rb_matplotlib = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.rb_matplotlib.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rb_matplotlib.setStyleSheet("color: rgb(255, 255, 255);\n"
                                         "font: 75 12pt \"Trebuchet MS\";")
        self.rb_matplotlib.setObjectName("rb_matplotlib")
        self.gridLayout_datos_grafica.addWidget(self.rb_matplotlib, 6, 0, 1, 1)

        self.rb_seaborn = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.rb_seaborn.setEnabled(True)
        self.rb_seaborn.setMinimumSize(QtCore.QSize(359, 0))
        self.rb_seaborn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.rb_seaborn.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 75 12pt \"Trebuchet MS\";")
        self.rb_seaborn.setObjectName("rb_seaborn")
        self.gridLayout_datos_grafica.addWidget(self.rb_seaborn, 7, 0, 1, 1)

        """
        
        Grupos
        
        """
        self.rb_group_tipo = QtWidgets.QButtonGroup()
        for i in [self.rb_pie, self.rb_linea, self.rb_barra]:
                self.rb_group_tipo.addButton(i)
        self.rb_group_libreria = QtWidgets.QButtonGroup()
        for i in [self.rb_seaborn, self.rb_matplotlib]:
                self.rb_group_libreria.addButton(i)


        """
        
                TItulo grafica,x,y
        
        """
        #titulo grafica

        self.lbl_titulo_grafica = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_titulo_grafica.setStyleSheet("font: 75 12pt \"Trebuchet MS\";\n"
                                              "color: rgb(255, 255, 255);")
        self.lbl_titulo_grafica.setObjectName("lbl_titulo_grafica")
        self.gridLayout_datos_grafica.addWidget(self.lbl_titulo_grafica, 8, 0, 1, 1)
        self.ipt_titulo_grafica = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ipt_titulo_grafica.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                              "font: 75 12pt \"Trebuchet MS\";color:black;")
        self.ipt_titulo_grafica.setObjectName("ipt_titulo_grafica")
        self.ipt_titulo_grafica.setMaxLength(70)
        self.gridLayout_datos_grafica.addWidget(self.ipt_titulo_grafica, 9, 0, 1, 1)



        #x

        self.lbl_eje_x = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_eje_x.setStyleSheet("font: 75 12pt \"Trebuchet MS\";\n"
                                     "color: rgb(255, 255, 255);")
        self.lbl_eje_x.setObjectName("lbl_eje_x")
        self.gridLayout_datos_grafica.addWidget(self.lbl_eje_x, 10, 0, 1, 1)

        self.ipt_eje_x = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ipt_eje_x.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "font: 75 12pt \"Trebuchet MS\";color:black;")
        self.ipt_eje_x.setObjectName("ipt_eje_x")
        self.ipt_eje_x.setMaxLength(50)
        self.gridLayout_datos_grafica.addWidget(self.ipt_eje_x, 11, 0, 1, 1)

        #y
        self.lbl_eje_y = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lbl_eje_y.setStyleSheet("font: 75 12pt \"Trebuchet MS\";\n"
                                     "color: rgb(255, 255, 255);")
        self.lbl_eje_y.setObjectName("lbl_eje_y")

        self.gridLayout_datos_grafica.addWidget(self.lbl_eje_y, 12, 0, 1, 1)
        self.ipt_eje_y = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.ipt_eje_y.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "font: 75 12pt \"Trebuchet MS\";color:black;")
        self.ipt_eje_y.setMaxLength(50)
        self.ipt_eje_y.setObjectName("ipt_eje_y")
        self.gridLayout_datos_grafica.addWidget(self.ipt_eje_y, 13, 0, 1, 1)







        """
        
        Boton generar
        
        """

        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(600, 730, 271, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_generar = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_generar.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_generar.setObjectName("gridLayout_generar")

        self.btn_generar_grafica = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_generar_grafica.setMinimumSize(QtCore.QSize(100, 60))
        self.btn_generar_grafica.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_generar_grafica.setStyleSheet("border: 1px solid #d0d0d0;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 16pt \"Trebuchet MS\";")
        self.btn_generar_grafica.setObjectName("btn_generar_grafica")
        self.gridLayout_generar.addWidget(self.btn_generar_grafica, 0, 0, 1, 1)

        """
        
        Boton configuracion anterior
        
        """
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(100, 750, 264, 80))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_configuracio_anterior = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_configuracio_anterior.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_configuracio_anterior.setObjectName("gridLayout_configuracio_anterior")
        self.btn_configuracion_anterior = QtWidgets.QPushButton(self.gridLayoutWidget_5)
        self.btn_configuracion_anterior.setMinimumSize(QtCore.QSize(200, 20))
        self.btn_configuracion_anterior.setMaximumSize(QtCore.QSize(200, 20))
        self.btn_configuracion_anterior.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_configuracion_anterior.setStyleSheet("border: 1px solid #d0d0d0;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"font: 75 12\n"
"pt \"Trebuchet MS\";")
        self.btn_configuracion_anterior.setObjectName("btn_configuracion_anterior")
        self.gridLayout_configuracio_anterior.addWidget(self.btn_configuracion_anterior, 0, 0, 1, 1)

        """
        
        Boton volver
        
        """
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(40, 10, 121, 31))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_volver = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_volver.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_volver.setObjectName("gridLayout_volver")
        self.btn_volver = QtWidgets.QPushButton(self.gridLayoutWidget_6)
        self.btn_volver.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_volver.setStyleSheet("border: 1px solid #d0d0d0;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"font: 75 16pt \"Trebuchet MS\";")
        self.btn_volver.setObjectName("btn_volver")
        self.gridLayout_volver.addWidget(self.btn_volver, 0, 0, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(590, 180, 311, 441))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")



        """
        
        Tabla items
        
        """
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tw_datos = QtWidgets.QTableWidget(self.gridLayoutWidget_3)
        self.tw_datos.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.tw_datos.setObjectName("tw_datos")
        self.tw_datos.setColumnCount(2)
        self.tw_datos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_datos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_datos.setHorizontalHeaderItem(1, item)
        self.gridLayout.addWidget(self.tw_datos, 0, 0, 1, 1)

        self.btn_otro_campo = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_otro_campo.setMinimumSize(QtCore.QSize(200, 20))
        self.btn_otro_campo.setMaximumSize(QtCore.QSize(200, 20))
        self.btn_otro_campo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_otro_campo.setStyleSheet("border: 1px solid #d0d0d0;\n"
                                                      "color: rgb(255, 255, 255);\n"
                                                      "background-color: rgb(0, 0, 0);\n"
                                                      "font: 75 12\n"
                                                      "pt \"Trebuchet MS\";")
        self.btn_otro_campo.setObjectName("btn_otro_campo")
        self.gridLayout.addWidget(self.btn_otro_campo, 2, 0, 1, 1)

        self.btn_limpiar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_limpiar.setMinimumSize(QtCore.QSize(200, 20))
        self.btn_limpiar.setMaximumSize(QtCore.QSize(200, 20))
        self.btn_limpiar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_limpiar.setStyleSheet("border: 1px solid #d0d0d0;\n"
                                          "color: rgb(255, 255, 255);\n"
                                          "background-color: rgb(0, 0, 0);\n"
                                          "font: 75 12\n"
                                          "pt \"Trebuchet MS\";")
        self.btn_limpiar.setObjectName("btn_limpiar")
        self.gridLayout.addWidget(self.btn_limpiar, 3, 0, 1, 1)

        pantalla_visualizador_graficas.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(pantalla_visualizador_graficas)
        self.statusbar.setObjectName("statusbar")
        pantalla_visualizador_graficas.setStatusBar(self.statusbar)

        self.retranslateUi(pantalla_visualizador_graficas)



        QtCore.QMetaObject.connectSlotsByName(pantalla_visualizador_graficas)
        pantalla_visualizador_graficas.setTabOrder(self.rb_barra, self.rb_linea)
        pantalla_visualizador_graficas.setTabOrder(self.rb_linea, self.rb_pie)
        pantalla_visualizador_graficas.setTabOrder(self.rb_pie, self.rb_matplotlib)
        pantalla_visualizador_graficas.setTabOrder(self.rb_matplotlib, self.rb_seaborn)
        pantalla_visualizador_graficas.setTabOrder(self.rb_seaborn, self.ipt_titulo_grafica)
        pantalla_visualizador_graficas.setTabOrder(self.ipt_titulo_grafica, self.ipt_eje_x)
        pantalla_visualizador_graficas.setTabOrder(self.ipt_eje_x, self.ipt_eje_y)
        pantalla_visualizador_graficas.setTabOrder(self.ipt_eje_y, self.tw_datos)
        pantalla_visualizador_graficas.setTabOrder(self.tw_datos, self.btn_generar_grafica)
        pantalla_visualizador_graficas.setTabOrder(self.btn_generar_grafica, self.btn_configuracion_anterior)
        pantalla_visualizador_graficas.setTabOrder(self.btn_configuracion_anterior, self.btn_volver)

    def retranslateUi(self, pantalla_visualizador_graficas):
        _translate = QtCore.QCoreApplication.translate
        pantalla_visualizador_graficas.setWindowTitle(_translate("pantalla_visualizador_graficas", "PIA-Generador de Gráficos"))

        self.lbl_introduzca.setText(_translate("pantalla_visualizador_graficas", "INTRODUZCA LOS DATOS Y TIPO DE GRÁFICA POR GENERAR"))
        self.lbl_titulo_grafica.setText(_translate("pantalla_visualizador_graficas", "TÍTULO DE LA GRÁFICA"))
        self.rb_matplotlib.setText(_translate("pantalla_visualizador_graficas", "MATPLOTLIB"))
        self.rb_pie.setText(_translate("pantalla_visualizador_graficas", "PÍE"))
        self.rb_seaborn.setText(_translate("pantalla_visualizador_graficas", "SEABORN"))
        self.lbl_eje_y.setText(_translate("pantalla_visualizador_graficas", "TÍTULO DEL EJE Y (OMITIR SI ES GRAFICA PIE)"))
        self.rb_linea.setText(_translate("pantalla_visualizador_graficas", "LÍNEA"))
        self.lbl_eje_x.setText(_translate("pantalla_visualizador_graficas", "TÍTULO DEL EJE X (OMITIR SI ES GRAFICA PIE)"))
        self.lbl_libreria.setText(_translate("pantalla_visualizador_graficas", "LIBRERIA"))
        self.rb_barra.setText(_translate("pantalla_visualizador_graficas", "BARRA"))
        self.lbl_tipo.setText(_translate("pantalla_visualizador_graficas", "TIPO DE GRÁFICO"))
        self.btn_generar_grafica.setText(_translate("pantalla_visualizador_graficas", "GENERAR GRÁFICA"))
        self.btn_configuracion_anterior.setText(_translate("pantalla_visualizador_graficas", "Usar Configuración Anterior"))
        self.btn_volver.setText(_translate("pantalla_visualizador_graficas", "Volver"))
        self.btn_otro_campo.setText(_translate("pantalla_visualizador_graficas","Agregar Otro Campo"))
        self.btn_limpiar.setText(_translate("pantalla_visualizador_graficas","Limpiar Componentes"))
        item = self.tw_datos.horizontalHeaderItem(0)
        item.setText(_translate("pantalla_visualizador_graficas", "X"))
        item = self.tw_datos.horizontalHeaderItem(1)
        item.setText(_translate("pantalla_visualizador_graficas", "Y"))
