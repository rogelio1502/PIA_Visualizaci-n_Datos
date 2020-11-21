import mysql.connector
from mensajes import showMessage,showdialog
#cambiar parametros de host,root,password segun sea sus credenciales del servidor MySql8

#funcion para crear base de datos
def crear_base_datos(db):
    try:
        my_db = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="susana15_A")
        cursor = _cursor(my_db)
        cursor.execute(f"CREATE DATABASE {db};")
        cursor.execute(f"USE {db};")
        cursor.execute("""
                CREATE TABLE configuracion_graficas(
                            id int primary key NOT NULL AUTO_INCREMENT,
                            titulo varchar(70) DEFAULT NULL,
                           titulo_x varchar(50) DEFAULT NULL,
                           valores_x text,
                           titulo_y varchar(50) DEFAULT NULL,
                           valores_y text,
                           tipo_grafica varchar(10) DEFAULT NULL,
                           libreria varchar(10) DEFAULT NULL,
                           comentarios varchar(250) DEFAULT NULL,
                           fecha datetime DEFAULT NULL


                );


            """)
        my_db.close()

    except mysql.connector.errors.Error as err:

        error = str(err)
        if error == "1007 (HY000): Can't create database 'graficas'; database exists":
            try:
                database=conectar(db)
                cursor = _cursor(database)
                insertar(database,cursor,"Hola","c","ca","dj","kdd","fdj","df","fd","2015-12-11 00:00:00")


            except:
                showMessage("Error","La base de datos no coincide con la tabla que necesita el programa\nTal Vez tiene el nombre igual a una de sus bases de datos pasada, si es así, cambie el nombre")
            else:
                eliminar(database,cursor,"2015-12-11 00:00:00")
            finally:
                database.close()
        else:
            showMessage("Error",str(err))
    except:
        showMessage("Error","Ha ocurrido un error desconocido al intentar crear la base de datos, favor de verificar parametros de conexion")





#funcion para conectarse con la base de datos
def conectar(db):
    try:
        my_db = mysql.connector.connect(host="localhost",
                                        user="root",
                                        password="susana15_A",
                                        database=db)
    except mysql.connector.errors.Error as err:
        showMessage("Error",str(err))
    except:
        _error = "Error al intentar conectarse con la base de datos. Favor de verificar los parametros de conexion con la base de datos."
        showMessage("ERROR", f"{_error}")
    else:
        return my_db
#funcion para definir un cursor de la conexion
def _cursor(my_db):
    try:

        mycursor = my_db.cursor()
    except mysql.connector.errors.Error as err:
        showMessage("Error",str(err))
    except:
        _error = "Error al intentar definir el cursor. Favor de verificar los parametros de conexion con la base de datos."
        showMessage("ERROR", f"{_error}")
    else:
        return mycursor

#funcion para insertar registros
def insertar(my_db,cursor,titulo,x,valores_x,y,valores_y,tipo,libreria,comentarios,fecha):
    valores_x_remix = ""
    valores_y_remix = ""
    for i in valores_x:
        valores_x_remix+=str(i)
        valores_x_remix+="|"
    for i in valores_y:
        valores_y_remix+=str(i)
        valores_y_remix+="|"
    try:
        values = (titulo,x,valores_x_remix,y,valores_y_remix,tipo,libreria,comentarios,fecha)
        sql =f"INSERT INTO configuracion_graficas (titulo,titulo_x,valores_x,titulo_y,valores_y,tipo_grafica,libreria,comentarios,fecha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        cursor.execute(sql, values)
        my_db.commit()
    except mysql.connector.errors.Error as err:
        showMessage("Error",str(err))
    except:
        _error = "Error al insertar el registro, asegurese de tener bien configurada la base de datos."
        showMessage("ERROR", f"{_error}")
    else:
        if fecha!="2015-12-11 00:00:00":

            mensaje = "SE HA GUARDADO LA TABLA CORRECTAMENTE"
            _done = showMessage("HECHO", f"{mensaje}")
#funcion para consultar registros
def consultar(cursor):
    sql = "SELECT fecha,titulo,tipo_grafica,libreria,titulo_x,valores_x,titulo_y,valores_y,comentarios FROM configuracion_graficas"
    try:
        cursor.execute(sql)
        graficas = cursor.fetchall()
    except mysql.connector.errors.Error as err:
        showMessage("Error",str(err))
    except:
        _error = "Error al consultar los registros, asegurese de tener bien configurada la base de datos."
        showMessage("ERROR", f"{_error}")
    else:
        return graficas
#funcion para eliminar registros
def eliminar(conexion,cursor,criterio):
    valores = (criterio,)
    sql = "DELETE FROM configuracion_graficas WHERE fecha=%s"
    try:
        cursor.execute(sql,valores)
        conexion.commit()
    except mysql.connector.errors.Error as err:
        showMessage("Error",str(err))
    except:
        _error = "Error al intentar eliminar los registros, asegurese de tener bien configurada la base de datos."
        showMessage("ERROR", f"{_error}")

    else:
        if criterio!="2015-12-11 00:00:00":

            _exito = "Configuración borrada correctamente."
            showMessage("ERROR", f"{_exito}")
#funcion para desconectarse de la base de datos
def desconectar(my_db):
    try:
        my_db.close()
    except mysql.connector.errors.Error as err:
        showMessage("Error",str(err))
    except:
        texto="Error al desconectarse de la base de datos."
        _error = showMessage("Error",texto)
