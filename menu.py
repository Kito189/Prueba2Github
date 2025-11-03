from login import iniciar_sesion
from orden_compra import gestionar_orden

def mostrar_menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Iniciar sesión")
        print("2. Gestionar órdenes de compra")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            gestionar_orden()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
