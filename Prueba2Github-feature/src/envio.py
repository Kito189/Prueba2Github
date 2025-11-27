from database import conectar_mysql

def despachar_producto():
    print("\n--- DESPACHO DE PRODUCTO ---")

    conexion = conectar_mysql()
    cur = conexion.cursor()

    factura_id = input("Ingrese el ID de la factura: ")
    comentario = input("Comentario del despacho: ")

    cur.execute("""
        INSERT INTO envios (factura_id, estado, comentario)
        VALUES (%s, 'despachado', %s)
    """, (factura_id, comentario))

    conexion.commit()

    print("Producto marcado como DESPACHADO 🚚")
