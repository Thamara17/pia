import sys
import mysql.connector 
from mysql.connector.errors import Error 

try:
    conn= None
    mi_cursor = None
    conn = mysql.conector.conect(user='pruebas python', password= '1234',
                             host='LOCALHOST',
                             database='clase_estructuras')
    mi_cursor = conn.cursor()

    datos = (6, "Don cangrejo")
    query = ("INSERT INTO conocido (Clave, Nombre) VALUES(%s,%s);")

    mi_cursor.execute(query, datos)
    conn.comit()
    print("El reguistro se agrego exitosamente")
except mysql.connector.Error as err:
    print(err)
except:
    print("fallo en la conexion")
finally:
    if(conn):
        conn.close()
        print("Se ha cerrado la conexion")
        if (mi_cursor):
            mi_cursor.close()
            print("se ha cerrado el cursor")