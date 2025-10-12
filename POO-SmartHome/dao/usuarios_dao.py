from conn.db_conn import ConexionDB
from domain.usuarios import Usuario

class UsuarioDAO:
    def __init__(self):
        self.db = ConexionDB()

    def registrar(self, usuario: Usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (email, nombre, clave, rol) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (usuario.get_email(), usuario.get_nombre(), usuario._Usuario__contrasena, usuario.get_rol()))
        conn.commit()
        print("Usuario registrado correctamente.")

    def login(self, login, clave):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """SELECT 
                 u.ID_USUARIO,
                 u.EMAIL,
                 u.NOMBRE,
                 u.LOGIN,
                 u.CLAVE,
                 r.NOMBRE AS NOMBRE_ROL
                 FROM USUARIOS u
                 JOIN ROLES r ON u.ROL = r.ID_ROL
                 WHERE u.LOGIN = %s;"""
        cursor.execute(sql, (login,))
        row = cursor.fetchone()
        if row and row['CLAVE'] == clave:
            return Usuario( row["ID_USUARIO"], row["EMAIL"], row["NOMBRE"], row["LOGIN"], row["CLAVE"], row["NOMBRE_ROL"])
        return None

    def cambiar_rol(self, id_usuario, nuevo_rol):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "UPDATE usuarios SET rol = %s WHERE id_usuario = %s"
        cursor.execute(sql, (nuevo_rol, id_usuario))
        conn.commit()
        print("Rol actualizado correctamente.")
        
    def listar_todos_usuarios(self):
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = """SELECT 
                    u.ID_USUARIO,
                    u.LOGIN,
                    u.NOMBRE AS NOMBRE_USUARIO,
                    u.EMAIL,
                    r.NOMBRE AS NOMBRE_ROL
                    FROM USUARIOS u
                    JOIN ROLES r ON u.ROL = r.ID_ROL;"""
            cursor.execute(sql)
            resultados = cursor.fetchall()

            usuarios = []
            for row in resultados:
                usuarios.append(Usuario(row['ID_USUARIO'],row['EMAIL'], row['NOMBRE_USUARIO'], row['LOGIN'],None, row['NOMBRE_ROL'])) 

            cursor.close()
            return usuarios
        


