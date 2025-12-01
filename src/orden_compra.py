from database import conectar_mysql

def gestionar_orden():
    print("\n--- Gestión de Órdenes de Compra ---")

    while True:
        print("\n1. Crear orden")
        print("2. Ver órdenes")
        print("3. Volver al menú")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = input("Número de orden: ")
            cliente = input("Cliente: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            comuna = input("Comuna: ")
            region = input("Región: ")
            producto = input("Producto: ")
            precio = input("Precio: ")

            try:
                conexion = conectar_mysql()
                cur = conexion.cursor()

                cur.execute("""
                    INSERT INTO ordenes_compra 
                    (numero_orden, cliente, direccion, telefono, comuna, region, producto, precio)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """, (numero, cliente, direccion, telefono, comuna, region, producto, precio))

                conexion.commit()
                print("Orden registrada con éxito ✔")

            except Exception as e:
                print("Error al guardar orden:", e)

            finally:
                if conexion:
                    conexion.close()

        elif opcion == "2":
            try:
                conexion = conectar_mysql()
                cur = conexion.cursor()

                cur.execute("SELECT * FROM ordenes_compra")
                datos = cur.fetchall()

                if not datos:
                    print("\nNo hay órdenes registradas.")
                else:
                    print("\n--- Órdenes registradas ---")
                    for o in datos:
                        print(f"ID: {o['id']} | Cliente: {o['cliente']} | Producto: {o['producto']} | Estado: {o['estado']} | Precio: {o['precio']}")

            except Exception as e:
                print("Error al cargar órdenes:", e)

            finally:
                if conexion:
                    conexion.close()

        elif opcion == "3":
            break

        else:
            print("Opción inválida.")

