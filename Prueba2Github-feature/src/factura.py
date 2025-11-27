from database import conectar_mysql

def emitir_factura():
    print("\n--- EMISIÓN DE FACTURA ---")

    conexion = conectar_mysql()
    cur = conexion.cursor()

    orden_id = input("Ingrese ID de la orden: ")

    # Obtener datos de la orden
    cur.execute("SELECT precio FROM ordenes_compra WHERE id=%s", (orden_id,))
    orden = cur.fetchone()

    if not orden:
        print("❌ No existe una orden con ese ID")
        return

    precio = float(orden["precio"])
    iva = round(precio * 0.19, 2)
    total = round(precio + iva, 2)

    # Crear factura
    cur.execute("""
        INSERT INTO facturas (orden_id, iva, total)
        VALUES (%s, %s, %s)
    """, (orden_id, iva, total))

    # Cambiar estado de la orden
    cur.execute("""
        UPDATE ordenes_compra
        SET estado = 'facturada'
        WHERE id = %s
    """, (orden_id,))

    conexion.commit()

    print(f"Factura creada con éxito ✔️")
    print(f"IVA: ${iva}")
    print(f"Total a pagar: ${total}")
