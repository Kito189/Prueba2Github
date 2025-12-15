from flask import Flask, request, jsonify
from flask_cors import CORS
from database import init_mysql

app = Flask(__name__)

# 🔥 CORS BIEN CONFIGURADO
CORS(app, supports_credentials=True)

# -----------------------------
# CONFIGURACIÓN MYSQL
# -----------------------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'proyecto_empresa'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = init_mysql(app)

# -----------------------------
# LOGIN (RF2)
# -----------------------------
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    cur = mysql.connection.cursor()
    cur.execute(
        "SELECT * FROM usuarios WHERE usuario=%s AND contrasena=%s",
        (data['usuario'], data['contrasena'])
    )
    user = cur.fetchone()
    cur.close()

    if user:
        return jsonify({"success": True}), 200
    return jsonify({"success": False}), 401


# -----------------------------
# ORDENES (RF1)
# -----------------------------
@app.route('/ordenes', methods=['GET'])
def listar_ordenes():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM ordenes_compra")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)


@app.route('/ordenes', methods=['POST'])
def crear_orden():
    data = request.get_json()

    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO ordenes_compra (cliente, producto, precio, estado)
        VALUES (%s, %s, %s, 'pendiente')
    """, (
        data['cliente'],
        data['producto'],
        data['precio']
    ))

    mysql.connection.commit()
    cur.close()

    return jsonify({"mensaje": "Orden creada"}), 201


# -----------------------------
# FACTURAS (RF4)
# -----------------------------
@app.route('/facturas', methods=['POST'])
def emitir_factura():
    data = request.get_json()
    orden_id = data['orden_id']

    cur = mysql.connection.cursor()
    cur.execute("SELECT precio FROM ordenes_compra WHERE id=%s", (orden_id,))
    orden = cur.fetchone()

    if not orden:
        return jsonify({"error": "Orden no existe"}), 404

    precio = float(orden['precio'])
    iva = round(precio * 0.19, 2)
    total = round(precio + iva, 2)

    cur.execute("""
        INSERT INTO facturas (orden_id, iva, total)
        VALUES (%s, %s, %s)
    """, (orden_id, iva, total))

    cur.execute("""
        UPDATE ordenes_compra SET estado='facturada' WHERE id=%s
    """, (orden_id,))

    mysql.connection.commit()
    cur.close()

    return jsonify({"mensaje": "Factura emitida"}), 201

@app.route('/facturas', methods=['GET'])
def listar_facturas():
    cur = mysql.connection.cursor()
    cur.execute("""
        SELECT f.id, f.orden_id, f.iva, f.total, f.fecha, f.estado
        FROM facturas f
        ORDER BY f.id DESC
    """)
    facturas = cur.fetchall()
    cur.close()
    return jsonify(facturas), 200



# -----------------------------
# ENVIOS (RF5)
# -----------------------------
@app.route('/envios', methods=['POST'])
def registrar_envio():
    data = request.get_json()

    cur = mysql.connection.cursor()
    cur.execute("""
        INSERT INTO envios (factura_id, comentario)
        VALUES (%s, %s)
    """, (
        data['factura_id'],
        data['comentario']
    ))

    mysql.connection.commit()
    cur.close()

    return jsonify({"mensaje": "Envío registrado"}), 201

@app.route('/envios', methods=['GET'])
def listar_envios():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM envios ORDER BY id DESC")
    envios = cur.fetchall()
    cur.close()
    return jsonify(envios), 200


# -----------------------------
# MAIN
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5000)
