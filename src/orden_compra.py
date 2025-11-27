def gestionar_orden():
    print("\n--- Gestión de Órdenes de Compra ---")
    ordenes = []

    while True:
        print("\n1. Crear orden")
        print("2. Ver órdenes")
        print("3. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            producto = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la cantidad: ")
            ordenes.append({"producto": producto, "cantidad": cantidad})
            print("Orden registrada con éxito ✅")
        elif opcion == "2":
            if not ordenes:
                print("No hay órdenes registradas.")
            else:
                print("\nÓrdenes registradas:")
                for i, o in enumerate(ordenes, 1):
                    print(f"{i}. {o['producto']} - {o['cantidad']} unidades")
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")
