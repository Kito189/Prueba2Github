from flask_mysqldb import MySQL

def init_mysql(app):
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'          
    app.config['MYSQL_PASSWORD'] = ''         
    app.config['MYSQL_DB'] = 'proyecto_empresa'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'  
    mysql = MySQL(app)
    return mysql
