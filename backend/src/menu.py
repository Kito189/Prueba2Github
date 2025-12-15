from login import iniciar_sesion
from orden_compra import gestionar_orden
from factura import emitir_factura
from envio import despachar_producto


def mostrar_menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Iniciar sesión")
        print("2. Gestionar órdenes de compra")
        print("3. Emitir factura")
        print("4. Despachar producto")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            iniciar_sesion()
        elif opcion == "2":
            gestionar_orden()
        elif opcion == "3":
            emitir_factura()
        elif opcion == "4":
            despachar_producto()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    mostrar_menu()
