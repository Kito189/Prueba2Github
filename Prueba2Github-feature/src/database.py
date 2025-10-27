from flask_mysqldb import MySQL

def init_mysql(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'          # o el usuario que uses en Laragon
    app.config['MYSQL_PASSWORD'] = ''          # pon tu contraseña si tienes una
    app.config['MYSQL_DB'] = 'proyecto_empresa'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  # devuelve resultados como diccionario
    mysql = MySQL(app)
    return mysql
