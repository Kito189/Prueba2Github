from database import conectar_mysql

def iniciar_sesion():
    print("\n--- Inicio de Sesión ---")
    usuario = input("Usuario: ")
    contrasena = input("Contraseña: ")

    try:
        conexion = conectar_mysql()
        cur = conexion.cursor()

        cur.execute("SELECT * FROM usuarios WHERE usuario=%s AND contrasena=%s",
                    (usuario, contrasena))
        resultado = cur.fetchone()

        if resultado:
            print("Inicio de sesión exitoso ✅")
            return True
        else:
            print("Credenciales incorrectas ❌")
            return False

    except Exception as e:
        print("Error al iniciar sesión:", e)

    finally:
        if conexion:
            conexion.close()
