import pymysql
from flask_mysqldb import MySQL

# --- para consola ---
def conectar_mysql():
    conexion = pymysql.connect(
        host='localhost',
        user='root',        # tu usuario de Laragon
        password='',        # tu contraseña si tienes
        database='proyecto_empresa',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conexion

# --- para Flask ---
def init_mysql(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'proyecto_empresa'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    mysql = MySQL(app)
    return mysql
