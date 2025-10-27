from flask import Flask, request, jsonify
from flask_cors import CORS
from database import init_mysql


app = Flask(__name__)
CORS(app)
mysql = init_mysql(app)

@app.route('/')
def home():
    return {'mensaje': 'Servidor Flask conectado correctamente 🚀'}


# ---------- LOGIN ----------
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contrasena')

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE usuario=%s AND contrasena=%s", (usuario, contrasena))
    user = cur.fetchone()
    cur.close()

    if user:
        return jsonify({"mensaje": "Inicio de sesión exitoso ✅"})
    else:
        return jsonify({"mensaje": "Credenciales incorrectas ❌"}), 401

# ---------- ORDENES ----------
@app.route('/ordenes', methods=['GET'])
def obtener_ordenes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ordenes")
    ordenes = cur.fetchall()
    cur.close()
    return jsonify(ordenes)

@app.route('/ordenes', methods=['POST'])
def crear_orden():
    data = request.get_json()
    producto = data.get('producto')
    cantidad = data.get('cantidad')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO ordenes (producto, cantidad) VALUES (%s, %s)", (producto, cantidad))
    mysql.connection.commit()
    cur.close()

    return jsonify({"mensaje": "Orden creada correctamente ✅"}), 201

if __name__ == '__main__':
    app.run(debug=True)

