from dao.usuarios_dao import UsuarioDAO
from dao.dispositivos_dao import DispositivoDAO
from dao.escenarios_dao import EscenarioDAO
from domain.usuarios import Usuario
from domain.dispositivos import Dispositivo
from domain.escenarios import Escenario


def menu_principal():
    print("""
    === MENÚ PRINCIPAL ===
    1. Registrarse
    2. Iniciar sesión
    0. Salir
    """)


def menu_admin():
    print("""
    === MENÚ ADMINISTRADOR ===
    1. Perfil
    2. Agregar dispositivo
    3. Listar dispositivos
    4. Cambiar estado del dispositivo
    5. Eliminar dispositivo
    6. Crear escenario
    7. Lista de usuarios
    8. Cambiar rol
    0. Cerrar sesion
    """)


def menu_invitado():
    print("""
    === MENÚ INVITADO ===
    1. Perfil
    2. Listar dispositivos
    0. Cerrar sesion
    """)


if __name__ == "__main__":
    usuario_dao = UsuarioDAO()
    dispositivo_dao = DispositivoDAO()
    escenario_dao = EscenarioDAO()
    usuario_actual = None


while True:
    menu_principal()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        email = input("Email: ")
        if usuario_dao.existe_email(email):
            print("Este email ya está registrado.")
        else:
            nombre = input("Nombre: ")
            login = input("Usuario: ")
            contrasena = input("Contraseña: ")
            usuario = Usuario(None, email, nombre, login, contrasena)
            usuario_dao.registrar(usuario)

    elif opcion == "2":
        login = input("usuario: ").strip()
        clave = input("Contraseña: ").strip()
        usuario_actual = usuario_dao.login(login, clave)

        if not usuario_actual:
            print("Credenciales inválidas.")
            continue
        rol = usuario_actual.get_rol()
        if rol == "Administrador":
            print(
                f"Bienvenido {usuario_actual.get_nombre()} Rol Administrador")
            while True:
                menu_admin()
                opcion = input("Seleccione una opción: ")

                if opcion == "1":
                    usuario_actual.mostrar_perfil()

                elif opcion == "2":
                    tipos_dispositivo = dispositivo_dao.listar_tipos_dispositivo()
                    print("\nTipos de dispositivo:")
                    for t in tipos_dispositivo:
                        print(
                            f"ID: {t.get_id_tipo_dispositivo()} | Nombre: {t.get_nombre_tipo()}")
                    tipo = int(input("ID Tipo dispositivo: "))

                    ubicaciones = dispositivo_dao.listar_ubicaciones()
                    print("\nUbicaciones:")
                    for u in ubicaciones:
                        print(
                            f"ID: {u.get_id_ubicacion()} | Nombre: {u.get_nombre()}")
                    ubicacion = int(input("ID Ubicación: "))

                    nombre = input("Nombre: ")
                    id_usuario = usuario_actual.get_id_usuario()
                    dispositivo = Dispositivo(
                        None, tipo, ubicacion, nombre, id_usuario)

                    dispositivo_dao.agregar_dispositivo(dispositivo)

                elif opcion == "3":
                    dispositivos = dispositivo_dao.listar_todos_dispositivos()
                    print("\nLista de dispositivos:")
                    for d in dispositivos:
                        print(
                            f"ID: {d.get_id_dispositivo()} | Nombre: {d.get_nombre()} | Tipo: {d.get_tipo()} | Ubicacion: {d.get_ubicacion()} | Estado: {d.get_estado()} | Usuario: {d.get_usuario()}")

                elif opcion == "4":
                    dispositivos = dispositivo_dao.listar_todos_dispositivos()
                    if not dispositivos:
                        print("No hay dispositivos registrados.")
                    else:
                        print("\n=== Lista de dispositivos ===")
                        for d in dispositivos:
                            print(f"ID: {d.get_id_dispositivo()} | Nombre: {d.get_nombre()} | Estado: {d.get_estado()}")

                        id_dispositivo = input("Ingrese el ID del dispositivo a modificar: ")
                        print("\n=== Estados disponibles ===")
                        cursor = dispositivo_dao.db.get_connection().cursor(dictionary=True)
                        cursor.execute("SELECT ID_ACCION, ACCION_DETALLE FROM ESTADODISPOSITIVO")
                        estados = cursor.fetchall()
                        for e in estados:
                            print(f"{e['ID_ACCION']} - {e['ACCION_DETALLE']}")
                        cursor.close()

                        nuevo_estado = input("Ingrese el ID del nuevo estado: ")
                        dispositivo_dao.editar_estado_dispositivo(id_dispositivo, nuevo_estado)

                elif opcion == "5":
                    dispositivos = dispositivo_dao.listar_todos_dispositivos()
                    if not dispositivos:
                        print("No hay dispositivos registrados.")
                    else:
                        print("\n=== Lista de dispositivos ===")
                        for d in dispositivos:
                            print(f"ID: {d.get_id_dispositivo()} | Nombre: {d.get_nombre()} | Tipo: {d.get_tipo()} | Ubicación: {d.get_ubicacion()} | Estado: {d.get_estado()}")

                        id_dispositivo = input("Ingrese el ID del dispositivo a eliminar: ")
                        confirmar = input(f"¿Seguro que querés eliminar el dispositivo con ID {id_dispositivo}? (s/n): ").lower()

                        if confirmar == "s":
                            dispositivo_dao.eliminar_dispositivo(id_dispositivo)
                        else:
                            print("Operación cancelada.")
                                
                elif opcion == "6":
                    nombre = input("Nombre del escenario: ")
                    descripcion = input("Descripción: ")
                    escenario = Escenario(None, nombre, descripcion)
                    escenario_dao.crear_escenario(escenario)

                elif opcion == "7":
                    usuarios = usuario_dao.listar_todos_usuarios()
                    print("\nLista de usuarios registrados:")
                    for u in usuarios:
                        print(
                            f"ID: {u.get_id_usuario()} | Nombre: {u.get_nombre()} | Email: {u.get_email()} | Rol: {u.get_rol()}")

                elif opcion == "8":
                    id_usuario = input("ID del usuario a modificar: ")
                    nuevo_rol = int(
                        input("1-Administrador\n2-Invitado\nElige una opcion: "))
                    usuario_dao.cambiar_rol(id_usuario, nuevo_rol)
                
                elif opcion == "9":
                    dispositivos = dispositivo_dao.listar_todos_dispositivos()
                    if not dispositivos:
                        print("No hay dispositivos registrados.")
                    else:
                        print("\n=== Lista de dispositivos ===")
                        for d in dispositivos:
                            print(f"ID: {d.get_id_dispositivo()} | Nombre: {d.get_nombre()} | Tipo: {d.get_tipo()} | Ubicación: {d.get_ubicacion()} | Estado: {d.get_estado()}")

                        id_dispositivo = input("Ingrese el ID del dispositivo a eliminar: ")
                        confirmar = input(f"¿Seguro que querés eliminar el dispositivo con ID {id_dispositivo}? (s/n): ").lower()

                        if confirmar == "s":
                            dispositivo_dao.eliminar_dispositivo(id_dispositivo)
                        else:
                            print("Operación cancelada.")

                elif opcion == "0":
                    print("Cerrando sesion")
                    break

                else:
                    print("Opción inválida.")
        elif rol == "Usuario":
            print(f"Bienvenido {usuario_actual.get_nombre()} Rol Invitado")
            while True:
                menu_invitado()
                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    usuario_actual.mostrar_perfil()

                elif opcion == "2":
                    dispositivos = dispositivo_dao.listar_todos_dispositivos()
                    print("\nLista de dispositivos:")
                    for d in dispositivos:
                        print(
                            f"ID: {d.get_id_dispositivo()} | Nombre: {d.get_nombre()} | Tipo: {d.get_tipo()} | Ubicacion: {d.get_ubicacion()} | Estado: {d.get_estado()} | Usuario: {d.get_usuario()}")

                elif opcion == "0":
                    print("Cerrando sesion")
                    break

                else:
                    print("Opción inválida.")

    elif opcion == "0":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida.")