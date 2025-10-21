from conn.db_conn import ConexionDB
from domain.usuarios import Usuario
import re 

class UsuarioDAO:
    def __init__(self):
        self.db = ConexionDB()

    def registrar(self, usuario: Usuario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO usuarios (usuario, email, nombre, CLAVE, rol) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (
            usuario.get_login(),
            usuario.get_email(),
            usuario.get_nombre(),
            usuario._Usuario__clave,
            usuario.get_rol()
        ))
        conn.commit()
        print("Usuario registrado correctamente.")
        cursor.close()

    def login(self, login, clave):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """SELECT 
                 u.ID_USUARIO,
                 u.EMAIL,
                 u.NOMBRE,
                 u.USUARIO,
                 u.CLAVE,
                 r.NOMBRE AS NOMBRE_ROL
                 FROM USUARIOS u
                 JOIN ROLES r ON u.ROL = r.ID_ROL
                 WHERE u.USUARIO = %s;"""
        cursor.execute(sql, (login,))
        row = cursor.fetchone()
        if row and row['CLAVE'] == clave:
            return Usuario( row["ID_USUARIO"], row["EMAIL"], row["NOMBRE"], row["USUARIO"], row["CLAVE"], row["NOMBRE_ROL"])
        cursor.close()
        return None

    def cambiar_rol(self, id_usuario, nuevo_rol):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "UPDATE usuarios SET rol = %s WHERE id_usuario = %s"
        cursor.execute(sql, (nuevo_rol, id_usuario))
        conn.commit()
        print("Rol actualizado correctamente.")
        cursor.close()
        
    def listar_todos_usuarios(self):
            conn = self.db.get_connection()
            cursor = conn.cursor(dictionary=True)
            sql = """SELECT 
                    u.ID_USUARIO,
                    u.USUARIO,
                    u.NOMBRE AS NOMBRE_USUARIO,
                    u.EMAIL,
                    r.NOMBRE AS NOMBRE_ROL
                    FROM USUARIOS u
                    JOIN ROLES r ON u.ROL = r.ID_ROL;"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            
            usuarios = []
            for row in resultados:
                usuarios.append(Usuario(row['ID_USUARIO'],row['EMAIL'], row['NOMBRE_USUARIO'], row['USUARIO'],None, row['NOMBRE_ROL'])) 

            cursor.close()
            return usuarios
    
    def existe_email(self, email):
            conn = self.db.get_connection()
            cursor = conn.cursor()
            sql = "SELECT COUNT(*) FROM usuarios WHERE email = %s"
            cursor.execute(sql, (email,))
            resultado = cursor.fetchone()
            cursor.close()
            return resultado[0] > 0
        
    def es_email_valido(self,email):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, email)
        


