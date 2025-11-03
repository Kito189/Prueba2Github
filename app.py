from flask import Flask, request, jsonify
from flask_cors import CORS
from database import init_mysql

# --- Inicialización del servidor Flask ---
app = Flask(__name__)
CORS(app)
mysql = init_mysql(app)


# --- Ruta principal ---
@app.route('/')
def home():
    return jsonify({"mensaje": "Servidor Flask conectado correctamente 🚀"})


# ==========================================================
# ==============   LOGIN (RF2)   ===========================
# ==========================================================
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    usuario = data.get('usuario')
    contrasena = data.get('contrasena')

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan credenciales"}), 400

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM usuarios WHERE usuario=%s AND contrasena=%s", (usuario, contrasena))
    user = cur.fetchone()
    cur.close()

    if user:
        return jsonify({"mensaje": "Inicio de sesión exitoso ✅"})
    else:
        return jsonify({"mensaje": "Credenciales incorrectas ❌"}), 401


# ==========================================================
# ==============   ÓRDENES DE COMPRA (RF1)   ===============
# ==========================================================

# 📋 Obtener todas las órdenes
@app.route('/ordenes', methods=['GET'])
def obtener_ordenes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ordenes_compra")
    ordenes = cur.fetchall()
    cur.close()

    if not ordenes:
        return jsonify({"mensaje": "No hay órdenes registradas."})
    return jsonify(ordenes)


# ➕ Crear una nueva orden
@app.route('/ordenes', methods=['POST'])
def crear_orden():
    data = request.get_json()

    campos_obligatorios = [
        "numero_orden", "cliente", "direccion", "telefono",
        "comuna", "region", "producto", "precio"
    ]

    # Validar que no falten campos
    for campo in campos_obligatorios:
        if campo not in data or data[campo] == "":
            return jsonify({"error": f"Falta el campo obligatorio: {campo}"}), 400

    numero_orden = data['numero_orden']
    cliente = data['cliente']
    direccion = data['direccion']
    telefono = data['telefono']
    comuna = data['comuna']
    region = data['region']
    producto = data['producto']
    precio = data['precio']

    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO ordenes_compra 
        (numero_orden, cliente, direccion, telefono, comuna, region, producto, precio)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (numero_orden, cliente, direccion, telefono, comuna, region, producto, precio))
    mysql.connection.commit()
    cur.close()

    return jsonify({"mensaje": "Orden creada correctamente ✅"}), 201


# ==========================================================
# ==============   Cierre seguro (RF3)   ===================
# ==========================================================

@app.route('/logout', methods=['POST'])
def logout():
    return jsonify({"mensaje": "Sesión cerrada correctamente 👋"})


# ==========================================================
# ==============   MAIN DEL SERVIDOR   =====================
# ==========================================================
if __name__ == '__main__':
    app.run(debug=True)
