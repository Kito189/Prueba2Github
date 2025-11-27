def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    if usuario == "admin" and contrasena == "1234":
        print("Inicio de sesión exitoso ✅")
    else:
        print("Credenciales incorrectas ❌")
