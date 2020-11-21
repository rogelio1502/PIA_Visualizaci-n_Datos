#librerias necesarias para el correcto funcionamiento del programa

from PyQt5.QtWidgets import QMessageBox
from PyQt5 import Qt,QtGui,QtWidgets
from mensajes import showMessage,showdialog,cerrar_ventana
from home import Ui_pantalla_visualizador_graficas
import matplotlib.pyplot as plt
import seaborn as sns
from comentarios_guardar import Guardar
from datetime import datetime
from configuraciones_guardadas import Configuracion
from conexion_base_datos import conectar,_cursor,desconectar,insertar,eliminar

#variables globales
global valores
global configuracion_tabla
global nombre_grafica
global comentarios_grabados
comentarios_grabados = ""
#funcion para determinar si un valor es entero
def es_entero(valor):
    try:
        valor = int(valor)
    except:
        return False
    else:
        return True
#funcion para determinar si un numero es flotante
def es_flotante(valor):
    try:
        valor =float(valor)
    except:
        return False
    else:
        return True
#nombre de la base de datos
bd = "graficas"

#clase principal de la ventana de captura de datos para visualizar grafica
class Home(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_pantalla_visualizador_graficas()
        self.ui.setupUi(self)
        #rellenamos la tabla con 6 valores
        self.fillTable(6)
        #damos conectividad a los botones
        self.ui.btn_generar_grafica.clicked.connect(self.validar)
        self.ui.btn_otro_campo.clicked.connect(self.generar_otro_campo)
        self.ui.btn_configuracion_anterior.clicked.connect(self.graficas_guardadas_ui)
        self.ui.btn_limpiar.clicked.connect(self.clean)
        #mostramos la pantalla
        self.show()
    #metodo para borrar contenido del qtablewidget
    def borrar_contenido(self):
        for i in reversed(range(self.ui.tw_datos.rowCount())):
            # por cada iteración, borramos la fila con indice del iterador
            self.ui.tw_datos.removeRow(i)
    #metodo para rellenar el qtablewidget con celdas vacias
    def fillTable(self,n):
        self.borrar_contenido()
        for i in range(n):
            # guardamos en una variable la posición de la fila en base a las filas
            rowPosition = self.ui.tw_datos.rowCount()
            # insertamos una fila en base a la variable anterior
            self.ui.tw_datos.insertRow(rowPosition)
            # obtenemos el numero de columnas
            numCols = self.ui.tw_datos.columnCount()
            # obtenemos el numero de filas
            numRows = self.ui.tw_datos.rowCount()
            # definimos el numero de filas
            self.ui.tw_datos.setRowCount(numRows)
            # definimos el numero de columnas
            self.ui.tw_datos.setColumnCount(numCols)
            for y in range(2):
                self.ui.tw_datos.setItem(numRows - 1, y, QtWidgets.QTableWidgetItem())
    #metodo para generar campos extra en el qtablewidget
    def generar_otro_campo(self):
        rowPosition = self.ui.tw_datos.rowCount()
        # insertamos una fila en base a la variable anterior
        self.ui.tw_datos.insertRow(rowPosition)
        # obtenemos el numero de columnas
        numCols = self.ui.tw_datos.columnCount()
        # obtenemos el numero de filas
        numRows = self.ui.tw_datos.rowCount()
        # definimos el numero de filas
        self.ui.tw_datos.setRowCount(numRows)
        # definimos el numero de columnas
        self.ui.tw_datos.setColumnCount(numCols)
        for y in range(2):

            self.ui.tw_datos.setItem(numRows - 1, y, QtWidgets.QTableWidgetItem())

    #metodo para validar los campos
    def validar(self):
        global configuracion_tabla
        global valores
        valores = []
        configuracion_tabla = []
        x = list()
        y = list()
        c_tipo=0
        c_libreria=0
        grafica = ""
        libreria = ""
        avanzar = False

        for i in self.ui.rb_group_tipo.buttons():
            if i.isChecked():
                grafica = grafica + i.text()
                c_tipo=+1
                break
        for i in self.ui.rb_group_libreria.buttons():
            if i.isChecked():
                libreria = libreria + i.text()
                c_libreria=+1
                break
        if c_tipo == 1 and c_libreria == 1:
            avanzar=True
        elif c_tipo == 0:
            showMessage("Error", "No se ha elegido el tipo de tabla.")
        elif c_libreria==0:
            showMessage("Error", "No se ha elegido la libreria.")





        if avanzar:
            titulo = self.ui.ipt_titulo_grafica.text()
            x_titulo = self.ui.ipt_eje_x.text()
            y_titulo = self.ui.ipt_eje_y.text()
            n = self.ui.tw_datos.rowCount()

            if len(titulo.replace(" ", "")) > 0:
                avanzar = True
            else:
                avanzar = False
                showMessage("Error", "Debe capturar el titulo de la gráfica correctamente")
        else:
            showMessage("Error", "No se ha elegido el tipo de libreria.")
        if avanzar:
            if grafica != "PÍE":

                if len(x_titulo.replace(" ", "")) > 0:
                    avanzar = True
                else:
                    avanzar = False
                    showMessage("Error", "Debe capturar el titulo de X correctamente.")
                if len(y_titulo.replace(" ", "")) > 0:
                    avanzar = True
                else:
                    avanzar = False
                    showMessage("Error", "Debe capturar el titulo de Y correctamente.")
            else:
                x_titulo = "No aplica"
                y_titulo = "No aplica"
        if avanzar:
            celdas_vacias = 0
            celdas_ocupadas = 0
            for i in range(n):
                _x = self.ui.tw_datos.item(i, 0).text()
                _y = self.ui.tw_datos.item(i, 1).text()
                if len(_x.replace(" ", "")) > 0 and (es_flotante(_y) or es_entero(_y)):
                    if celdas_vacias == 1:
                        showMessage("Error", "Hay lugares sin llenar,Recuerde que los registros deben ser seguidos.")
                        avanzar = False
                        x = []
                        y = []
                        break
                    else:

                        x.append(_x)
                        y.append(float(_y))
                        celdas_ocupadas = celdas_ocupadas + 1

                elif (len(_x.replace(" ", "")) == 0 and (es_flotante(_y) or es_entero(_y))):
                    showMessage("Error", f"Valor de la columna X de la fila {i + 1} sin llenar")
                    avanzar = False
                    break
                elif (len(_x.replace(" ", "")) > 0 and (es_flotante(_y) == False and es_entero(_y)==False)):
                    showMessage("Error", f"Valor de la columna Y de la fila {i + 1} no valido")
                    avanzar = False
                    break
                elif (len(_x.replace(" ", "")) > 0 and len(_y.replace(" ", "")) == 0):
                    showMessage("Error", f"Valor de la columna Y de la fila {i + 1} no ingresado")
                    avanzar = False
                    break
                elif len(_x.replace(" ", "")) == 0 and len(_y.replace(" ", "")) == 0:
                    celdas_vacias = +1

            avanzar_tabla = False
            print(celdas_ocupadas)
            if celdas_ocupadas >= 1:
                valores.append(x)
                valores.append(y)
                avanzar_tabla = True
            elif celdas_ocupadas < 1:
                showMessage("Error", "No hay valores capturados.")
                avanzar = False
        #si todo es correcto lo añadimos a configuracion_tabla
        if avanzar and avanzar_tabla:
            configuracion_tabla.append(titulo)
            configuracion_tabla.append(x_titulo)
            configuracion_tabla.append(y_titulo)
            configuracion_tabla.append(valores)
            configuracion_tabla.append(grafica)
            configuracion_tabla.append(libreria)
            #llamamos a generar grafica para que valide la configuracion una vez mas y genere la tabla
            self.generar_grafica()




    #metodo para generar una grafica en base a configuracion lista
    def generar_grafica(self):
        global configuracion_tabla
        global valores
        global nombre_grafica


        if len(configuracion_tabla) == 6:
            #guardamos la configuracion en un diccionario
            diccionario_configuracion = {
                "Titulo gráfica": configuracion_tabla[0],
                "Titulo X": configuracion_tabla[1],
                "Valores X": configuracion_tabla[3][0],
                "Titulo Y": configuracion_tabla[2],
                "Valores Y": configuracion_tabla[3][1],
                "Tipo de gráfica": configuracion_tabla[4],
                "Librería": configuracion_tabla[5]

            }
            #print(diccionario_configuracion)
            #mandamos ensaje para ver si el usuario quiere generar la grafica
            if len(configuracion_tabla[3][0])>1:

                generar = showdialog("ATENCION", "¿DESEA GENERAR LA GRÁFICA CON LA CONFIGURACIÓN ELEGIDA?")
                # si elige si
                if generar == 1024:
                    # cerramos graficas anteriores
                    try:
                        plt.close()
                        self.guardar.close()
                    except:
                        pass
                    # vaciamos el nombre de la grafica que eligio para imprimirlo en la pantalla de comentarios
                    nombre_grafica = configuracion_tabla[0]
                    # dependiendo la libreria se genera la grafica


                    #matplotlib
                    if diccionario_configuracion["Librería"].upper() == "MATPLOTLIB":
                        print("Matplot")
                        if diccionario_configuracion["Tipo de gráfica"].upper() == "BARRA":
                            fig, ax = plt.subplots(1, figsize=(8, 6))
                            ax.set_title(diccionario_configuracion['Titulo gráfica'], fontsize=16)
                            ax.bar(diccionario_configuracion['Valores X'], diccionario_configuracion['Valores Y'],
                                   edgecolor='black')
                            ax.set_xlabel(diccionario_configuracion['Titulo X'])
                            ax.set_ylabel(diccionario_configuracion['Titulo Y'])
                            fig.legend([ax],  # List of the line objects
                                       labels=[diccionario_configuracion['Titulo Y']],  # The labels for each line
                                       loc="center right",  # Position of the legend
                                       borderaxespad=0.1,  # Add little spacing around the legend box
                                       title="Leyenda")  # Title for the legend
                            rects = ax.patches
                            labels = ["%d" % i for i in diccionario_configuracion['Valores Y']]
                            print(labels)
                            for rect, label in zip(rects,labels):
                                height=rect.get_height()
                                ax.text(rect.get_x() + rect.get_width()/2, height + 1, label, ha='center', va='bottom')
                            plt.subplots_adjust(right=0.85)
                            plt.show()

                            self.guardar_ui()
                        if diccionario_configuracion["Tipo de gráfica"].upper() == "LÍNEA":
                            print("Hola")
                            fig, ax = plt.subplots(1, figsize=(8, 6))
                            fig.suptitle(diccionario_configuracion['Titulo gráfica'], fontsize=15)
                            ax.plot(diccionario_configuracion['Valores X'], diccionario_configuracion['Valores Y'],
                                    "-o", linestyle="dashed", label=diccionario_configuracion['Titulo Y'])
                            ax.set_xlabel(diccionario_configuracion['Titulo X'])
                            ax.set_ylabel(diccionario_configuracion['Titulo Y'])
                            ax.legend(loc="upper right", title="Leyenda", frameon=False)
                            plt.show()
                            self.guardar_ui()
                        if diccionario_configuracion["Tipo de gráfica"].upper() == "PÍE":
                            showMessage("INFO", "Titulo de X e Y no aplican para esta gráfica, se omitirán.")
                            plt.pie(diccionario_configuracion['Valores Y'],
                                    labels=diccionario_configuracion['Valores X'], autopct='%1.1f%%', shadow=True,
                                    startangle=90)
                            plt.title(diccionario_configuracion['Titulo gráfica'])
                            plt.show()
                            self.guardar_ui()

                    #seaborn
                    elif configuracion_tabla[-1].upper() == "SEABORN":
                        if diccionario_configuracion["Tipo de gráfica"].upper() == "BARRA":
                            data = {diccionario_configuracion['Titulo X']: diccionario_configuracion['Valores X'],
                                    diccionario_configuracion['Titulo Y']: diccionario_configuracion['Valores Y']}

                            sns.set_theme(style="darkgrid")

                            sns.barplot(x=diccionario_configuracion['Titulo X'],
                                        y=diccionario_configuracion['Titulo Y'], data=data)


                            plt.title(diccionario_configuracion['Titulo gráfica'])
                            plt.show()
                            self.guardar_ui()
                        if diccionario_configuracion["Tipo de gráfica"].upper() == "LÍNEA":
                            data = {diccionario_configuracion['Titulo X']: diccionario_configuracion['Valores X'],
                                    diccionario_configuracion['Titulo Y']: diccionario_configuracion['Valores Y']}
                            sns.set_theme(style="darkgrid")
                            sns.lineplot(x=diccionario_configuracion['Titulo X'],
                                         y=diccionario_configuracion['Titulo Y'], data=data, marker="o")
                            plt.title(diccionario_configuracion['Titulo gráfica'])
                            plt.show()
                            self.guardar_ui()

                        if diccionario_configuracion["Tipo de gráfica"].upper() == "PÍE":
                            showMessage("INFO", "Titulo de X e Y no aplican para esta gráfica, se omitirán.")
                            sns.set_theme(style="darkgrid")
                            plt.pie(diccionario_configuracion['Valores Y'],
                                    labels=diccionario_configuracion['Valores X'],
                                    autopct='%1.1f%%', shadow=True, startangle=90)
                            plt.title(diccionario_configuracion['Titulo gráfica'])
                            plt.show()
                            self.guardar_ui()
            else:
                showMessage("Error","No es posible generar una grafica de un solo valor")



        else:
            showMessage("Error", "No se han capturado los valores por completo.")
            configuracion_tabla.pop(5)
            configuracion_tabla.pop(4)
    #metodo que instancia la clase configuracion para asi poder abrir una pantalla con las configuraciones guardadas
    def graficas_guardadas_ui(self):
        self.guardadas = Configuracion()
        self.guardadas.ui.btn_consultar.clicked.connect(self.rellenar)
        self.guardadas.ui.btn_eliminar.clicked.connect(self.eliminar_datos)
        self.guardadas.show()
    #metodo que instancia la clase guardar para asi poder abrir la pantalla de comentarios y guardar
    def guardar_ui(self):
        global comentarios_grabados
        self.guardar = Guardar(nombre_grafica)
        if len(comentarios_grabados)>0:
            self.guardar.ui.ipt_comentarios.setText(comentarios_grabados)
        self.guardar.ui.btn_guardar.clicked.connect(self.guardar_datos)
        self.guardar.show()
    #metodo para guardar los datos
    def guardar_datos(self):

        titulo= configuracion_tabla[0]
        titulo_x= configuracion_tabla[1]
        valores_x= configuracion_tabla[3][0]
        titulo_y = configuracion_tabla[2]
        valores_y= configuracion_tabla[3][1]
        valores_y = valores_y
        tipo_grafica = configuracion_tabla[4]
        libreria = configuracion_tabla[5]
        comentarios = self.guardar.ui.ipt_comentarios.toPlainText()
        fecha = datetime.now()
        guardar = False
        print(len(comentarios))


        if len(comentarios)==0 :
            continuar = showdialog("Error","No se agregaran comentarios. ¿Desea Guardar?")
            if continuar == 1024:
                guardar = True
            else:
                guardar = False
        else:
            if len(comentarios)<250:

                guardar=True
            else:
                showMessage("Error","No puede tener una longitud de mas de 250 caracteres el texto de comentarios\n"\
                            f"Usted introdujo {len(comentarios)}")

        if guardar:
            try:

                conexion = conectar(bd)
                cursor = _cursor(conexion)
                insertar(conexion,cursor,titulo,titulo_x,valores_x,titulo_y,valores_y,tipo_grafica,libreria,comentarios,fecha)
                desconectar(conexion)
            except:
                pass
            else:
                self.guardar.close()
                plt.close()
                self.clean()


    def clean(self):
        self.fillTable(6)
        self.ui.ipt_titulo_grafica.setText("")
        self.ui.ipt_eje_x.setText("")
        self.ui.ipt_eje_y.setText("")
    #evento para controlar el cerrado de ventana, si es pulsado el boton de cerrar, se pregunta al usuario si desea
    #cerrarla, si es así, se cierra la ventana
    def closeEvent(self, event):

        valor = cerrar_ventana(self,event)
        if valor == 16384:

            try:
                self.guardadas.close()
            except:
                pass
            try:
                self.guardar.close()

            except:
                pass
            try:
                plt.close()
            except:
                pass
    #metodo para tomar los valores de graficas anteriores y rellenar el qtablewidget principal y los
    #componentess del generador de graficas
    def rellenar(self):
        global comentarios_grabados
        valores = []
        valores_x = []
        valores_y = []
        numRows = self.guardadas.ui.tabla_graficas.rowCount()
        if numRows>0:
            try:
                fila = (self.guardadas.ui.tabla_graficas.currentRow())
                for i in range(9):

                    if i == 5:

                        cb = self.guardadas.ui.tabla_graficas.cellWidget(fila, i)
                        for y in range(len(cb)):
                            valores_x.append(cb.itemText(y))
                        valores.append(valores_x)
                    elif i == 7:
                        cb = self.guardadas.ui.tabla_graficas.cellWidget(fila, i)
                        for y in range(len(cb)):
                            valores_y.append(cb.itemText(y))
                        valores.append(valores_y)
                    elif i != 5 and i != 7:

                        valores.append(self.guardadas.ui.tabla_graficas.item(fila, i).text())

                print(valores)

                for i in self.ui.rb_group_tipo.buttons():
                    if i.text() == valores[2]:
                        i.setChecked(True)

                for i in self.ui.rb_group_libreria.buttons():
                    if i.text() == valores[3]:
                        i.setChecked(True)
                comentarios_grabados = valores[8]
                self.ui.ipt_titulo_grafica.setText(valores[1])
                self.ui.ipt_eje_x.setText(valores[4])
                self.ui.ipt_eje_y.setText(valores[6])
                self.borrar_contenido()
                n = len(valores[5])
                self.fillTable(n)
                for i in range(n):
                    self.ui.tw_datos.setItem(i, 0, QtWidgets.QTableWidgetItem(str(valores[5][i])))
                    self.ui.tw_datos.setItem(i, 1, QtWidgets.QTableWidgetItem(str(valores[7][i])))

                self.guardadas.close()
            except:
                showMessage("Error","No ha seleccionado ningún registro")




        else:
            showMessage("Error", "No hay registros")
    #metodo para eliminar los datos de la configuracion de alguna grafica guardada
    def eliminar_datos(self):

        numRows = self.guardadas.ui.tabla_graficas.rowCount()
        if numRows>0:

            index = (self.guardadas.ui.tabla_graficas.currentRow())
            print(index)
            if index>-1:
                delete = showdialog("Advertencia",f"Desea eliminar el registro de la fila {index+1}")
                if delete == 1024:
                    try:
                        fecha = self.guardadas.ui.tabla_graficas.item(index, 0).text()
                        conexion = conectar(bd)
                        cursor = _cursor(conexion)
                        eliminar(conexion, cursor, fecha)
                        desconectar(conexion)
                    except:
                        pass
                    else:
                        self.guardadas.fillTable()
            else:
                showMessage("Error", "Ningun registro ha sido seleccionado")





        else:
            showMessage("Error","No hay ningún registro aún")
