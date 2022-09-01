from hashlib import new
import pymysql

def conectar():

    conn=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='',
    db='comprobante_sri'
    )
    print("Conexion Exitosa")
    info_server=conn.get_server_info()
    cursor = conn.cursor()
    cursor.execute("show databases")

    row = cursor.fetchone()
    print("Conectado a la base de datos: {}".format(row))


