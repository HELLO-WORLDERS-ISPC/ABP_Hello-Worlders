from dao.usuarios_dao import UsuarioDAO
from dao.dispositivos_dao import DispositivoDAO
from domain.usuarios import Usuario
from domain.dispositivos import Dispositivo
from typing import Optional


def rol_id_por_nombre(nombre: str) -> int:
    # Ajusta si tus IDs difieren. Asumo: 1=ADMIN, 2=INVITADO
    return 1 if nombre.lower() in ("admin","administrador") else 2


# ===== Menús =====
def menu_publico() -> str:
    print("\n=== SmartHome Solutions ===")
    print("1) Registrarse")
    print("2) Iniciar sesión")
    print("0) Salir")
    return input("> ").strip()

def registrar(udao: UsuarioDAO):
    print("\n-- Registro --")
    login = input("Login (usuario/email): ").strip()
    nombre = input("Nombre: ").strip()
    email  = input("Email (opcional): ").strip() or None
    clave  = input("Clave: ").strip()
    rol    = "invitado"  # por defecto
    uid = udao.crear(Usuario(None, login, nombre, clave, rol_id_por_nombre(rol), email))
    print(f"✅ Usuario creado con id {uid}")

def iniciar_sesion(udao: UsuarioDAO) -> Optional[Usuario]:
    print("\n-- Login --")
    login = input("Login: ").strip()
    clave = input("Clave: ").strip()
    u = udao.verificar_login(login, clave)
    if not u:
        print("❌ Credenciales inválidas")
        return None
    print(f"✅ Bienvenido {u.nombre} (rol: {u.rol_nombre})")
    return u

def menu_usuario(u: Usuario, ddao: DispositivoDAO):
    while True:
        print("\n--- Menú Usuario ---")
        print("1) Ver mis datos")
        print("2) Ver mis dispositivos")
        print("0) Cerrar sesión")
        op = input("> ").strip()
        if op == "1":
            print(f"ID:{u.id_usuario} | Login:{u.login} | Nombre:{u.nombre} | Email:{u.email} | Rol:{u.rol_nombre}")
        elif op == "2":
            devs = ddao.listar_por_usuario(u.id_usuario)
            if not devs:
                print("No tenés dispositivos.")
            else:
                for r in devs:
                    est = "ON" if r["ESTADO"] else "OFF"
                    print(f"[{r['ID_DISPOSITIVO']}] {r['NOMBRE_DISPOSITIVO']} ({r['NOMBRE_TIPO']}) - {est} @ {r['UBICACION_NOMBRE']}")
        elif op == "0":
            break

def crear_dispositivo_rapido(u: Usuario, ddao: DispositivoDAO):
    print("\n-- Crear dispositivo (demo) --")
    nombre = input("Nombre: ").strip()
    tipo_id = int(input("ID tipo (ej 1=luz): ").strip())
    ubic_id = int(input("ID ubicación (ej 1=Living): ").strip())
    accion  = int(input("ID acción (ej 1=ENCENDER): ").strip())
    encendido = input("¿Encendido? (s/n): ").strip().lower().startswith("s")
    did = ddao.crear(Dispositivo(None, nombre, tipo_id, u.id_usuario, ubic_id, accion, encendido))
    print(f"✅ Dispositivo creado ID {did}")

def menu_admin(u: Usuario, ddao: DispositivoDAO, udao: UsuarioDAO):
    while True:
        print("\n--- Menú Admin ---")
        print("1) Ver mis dispositivos")
        print("2) Crear dispositivo rápido (demo)")
        print("3) Cambiar rol de un usuario")
        print("0) Cerrar sesión")
        op = input("> ").strip()
        if op == "1":
            devs = ddao.listar_por_usuario(u.id_usuario)
            for r in devs:
                est = "ON" if r["ESTADO"] else "OFF"
                print(f"[{r['ID_DISPOSITIVO']}] {r['NOMBRE_DISPOSITIVO']} ({r['NOMBRE_TIPO']}) - {est} @ {r['UBICACION_NOMBRE']}")
        elif op == "2":
            crear_dispositivo_rapido(u, ddao)
        elif op == "3":
            uid = int(input("ID usuario: ").strip())
            nuevo = input("Nuevo rol (admin/invitado): ").strip()
            ok = udao.cambiar_rol(uid, rol_id_por_nombre(nuevo))
            print("✅ Rol actualizado" if ok else "❌ No se pudo actualizar")
        elif op == "0":
            break


# ===== App loop =====
def run():
    udao = UsuarioDAO()
    ddao = DispositivoDAO()

    while True:
        op = menu_publico()
        if op == "1":
            registrar(udao)
        elif op == "2":
            u = iniciar_sesion(udao)
            if not u:
                continue
            if (u.rol_nombre or "").lower() in ("admin", "administrador"):
                menu_admin(u, ddao, udao)
            else:
                menu_usuario(u, ddao)
        elif op == "0":
            print("👋 Hasta luego!")
            break
        else:
            print("Opción inválida")

if __name__ == "__main__":
    run()