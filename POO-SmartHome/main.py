from dao.usuarios_dao import UsuarioDAO
from dao.dispositivos_dao import DispositivoDAO
from dao.escenarios_dao import EscenarioDAO
from domain.usuarios import Usuario
from domain.dispositivos import Dispositivo
from domain.escenarios import Escenario

def menu_prinsipal():
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
    3. Crear escenario
    4. Lista de usuarios
    5. Cambiar rol
    0. Cerrar sesion
    """)
def menu_invitado():
    print("""
    === MENÚ INVITADO ===
    1. Perfil
    2. Agregar dispositivo
    0. Cerrar sesion
    """)

if __name__ == "__main__":
    usuario_dao = UsuarioDAO()
    dispositivo_dao = DispositivoDAO()
    escenario_dao = EscenarioDAO()
    usuario_actual = None

            
while True:
        menu_prinsipal()
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
            rol = usuario_actual.get_rol()
            if usuario_actual != None:
                if rol == "Administrador":
                    print(f"Bienvenido {usuario_actual.get_nombre()} Rol Administrador")
                    while True:
                        menu_admin()
                        opcion = input("Seleccione una opción: ")
                        
                        if opcion == "1":
                            usuario_actual.mostrar_perfil()

                        elif opcion == "2":
                                tipo = input("Tipo de dispositivo: ")
                                ubicacion = input("Ubicación: ")
                                nombre = input("Nombre: ")
                                dispositivo = Dispositivo(tipo, ubicacion, nombre)
                                dispositivo_dao.agregar_dispositivo(dispositivo)

                        elif opcion == "3":
                                nombre = input("Nombre del escenario: ")
                                descripcion = input("Descripción: ")
                                escenario = Escenario(None, nombre, descripcion)
                                escenario_dao.crear_escenario(escenario)
                        
                        elif opcion == "4": 
                            usuarios = usuario_dao.listar_todos_usuarios()
                            print("\nLista de usuarios registrados:")
                            for u in usuarios:
                                print(f"ID: {u.get_id_usuario()} | Nombre: {u.get_nombre()} | Email: {u.get_email()} | Rol: {u.get_rol()}")
                        
                        elif opcion == "5":
                                id_usuario = input("ID del usuario a modificar: ")
                                nuevo_rol = int(input("1-Administrador\n2-Invitado\nElige una opcion: "))
                                usuario_dao.cambiar_rol(id_usuario, nuevo_rol)

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
                                tipo = input("Tipo de dispositivo: ")
                                ubicacion = input("Ubicación: ")
                                nombre = input("Nombre: ")
                                dispositivo = Dispositivo(tipo, ubicacion, nombre)
                                dispositivo_dao.agregar_dispositivo(dispositivo)

                        elif opcion == "0":
                            print("Cerrando sesion")
                            break

                        else:
                            print("Opción inválida.")
            else:
                print("Credenciales inválidas.")

        elif opcion == "0":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")
            