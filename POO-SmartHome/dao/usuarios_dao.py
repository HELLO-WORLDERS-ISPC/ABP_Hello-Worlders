# dao/usuario_dao.py
from typing import Optional, List
from conn.db_conn import ConexionDB
from domain.usuarios import Usuario
import hashlib

class UsuarioDAO:
    def __init__(self):
        self.db = ConexionDB()

    def crear(self, u: Usuario) -> int:
        cur = self.db.get_cursor()
        hashed = hashlib.sha256(u.clave.encode()).hexdigest()
        sql = """INSERT INTO USUARIOS (LOGIN, NOMBRE, CLAVE, ROL, EMAIL)
                VALUES (%s,%s,%s,%s,%s)"""
        cur.execute(sql, (u.login, u.nombre, hashed, u.rol_id, u.email))
        self.db.commit()
        new_id = cur.lastrowid
        self.db.close()
        return new_id
    
    def verificar_login(self, login: str, clave: str) -> Optional[Usuario]:
      cur = self.db.get_cursor()
      cur.execute("SELECT * FROM USUARIOS WHERE LOGIN=%s", (login,))
      row = cur.fetchone()
      self.db.close()
      if not row:
          return None
      hashed = hashlib.sha256(clave.encode()).hexdigest()
      if row["CLAVE"] == hashed:
          return Usuario(row["ID_USUARIO"], row["LOGIN"], row["NOMBRE"], row["CLAVE"], row["ROL"], row["EMAIL"])
      return None

    def obtener_por_login(self, login: str) -> Optional[Usuario]:
        cur = self.db.get_cursor()
        sql = """SELECT u.ID_USUARIO, u.LOGIN, u.NOMBRE, u.CLAVE, u.ROL, u.EMAIL, r.NOMBRE AS ROL_NOMBRE
                FROM USUARIOS u
                JOIN ROLES r ON u.ROL = r.ID_ROL
                WHERE u.LOGIN = %s"""
        cur.execute(sql, (login,))
        row = cur.fetchone()
        self.db.close()
        if not row: return None
        return Usuario(
            row["ID_USUARIO"], row["LOGIN"], row["NOMBRE"], row["CLAVE"],
            row["ROL"], row["EMAIL"], row["ROL_NOMBRE"]
        )

    def listar(self, limite=50, offset=0) -> List[Usuario]:
        cur = self.db.get_cursor()
        sql = """SELECT u.ID_USUARIO, u.LOGIN, u.NOMBRE, u.CLAVE, u.ROL, u.EMAIL, r.NOMBRE AS ROL_NOMBRE
                FROM USUARIOS u
                JOIN ROLES r ON u.ROL = r.ID_ROL
                ORDER BY u.ID_USUARIO DESC
                LIMIT %s OFFSET %s"""
        cur.execute(sql, (limite, offset))
        rows = cur.fetchall()
        self.db.close()
        return [Usuario(r["ID_USUARIO"], r["LOGIN"], r["NOMBRE"], r["CLAVE"], r["ROL"], r["EMAIL"], r["ROL_NOMBRE"]) for r in rows]

    def actualizar(self, u: Usuario) -> bool:
        assert u.id_usuario is not None
        cur = self.db.get_cursor()
        sql = """UPDATE USUARIOS
                SET LOGIN=%s, NOMBRE=%s, CLAVE=%s, ROL=%s, EMAIL=%s
                WHERE ID_USUARIO=%s"""
        cur.execute(sql, (u.login, u.nombre, u.clave, u.rol_id, u.email, u.id_usuario))
        self.db.commit()
        ok = cur.rowcount > 0
        self.db.close()
        return ok

    def cambiar_rol(self, id_usuario: int, rol_id: int) -> bool:
        cur = self.db.get_cursor()
        cur.execute("UPDATE USUARIOS SET ROL=%s WHERE ID_USUARIO=%s", (rol_id, id_usuario))
        self.db.commit()
        ok = cur.rowcount > 0
        self.db.close()
        return ok

    def eliminar(self, id_usuario: int) -> bool:
        cur = self.db.get_cursor()
        cur.execute("DELETE FROM USUARIOS WHERE ID_USUARIO=%s", (id_usuario,))
        self.db.commit()
        ok = cur.rowcount > 0
        self.db.close()
        return ok
