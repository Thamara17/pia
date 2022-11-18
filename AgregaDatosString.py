from fileinput import close
import sys
from telnetlib import EOR
import mysql.connector
from mysql.connector.errors import Error
#Agrega datos a una tabla, ultiliza integracion de cadena(No es recomendable)

try:
    conn = None
    mi_cursor = None
    conn = mysql.connector.connect(user'pruebasPython',password = '1234',
                              host='LOCALHOST',
                              database='clase_estructuras')
mi_cursor = conn.cursor()

datos = {"clave":5,"nombre":"Patrick"}
query = (f"INSERT INTO conocido (Clave,Nombre) VALUES ({datos['clave')

mi_cursor.execute(query, datos)
conn.commit()
print("El registro se agregó exitosamente")
except mysql.connector.Error as err:
    print(err)
except:
    print("Fallo en la conexion")
finally:
    if(conn):
        conn.close()
        print("Se ha cerrado la conexion")
        if(mi_cursor):
           mi_cursor.close()
           print("Se ha cerrado el cursor")
           