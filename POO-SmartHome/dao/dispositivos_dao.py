# dao/dispositivo_dao.py
from typing import Optional, List
from conn.db_conn import ConexionDB
from domain.dispositivos import Dispositivo

class DispositivoDAO:
    def __init__(self):
        self.db = ConexionDB()

    def crear(self, d: Dispositivo) -> int:
        cur = self.db.get_cursor()
        sql = """INSERT INTO DISPOSITIVOS (NOMBRE_DISPOSITIVO, ID_ACCION, ID_TIPO_DISPOSITIVO, ID_USUARIO, ID_UBICACION{estado_col})
                VALUES (%s,%s,%s,%s,%s{estado_val})""".format(
            estado_col=", ESTADO" if hasattr(d, "estado") else "",
            estado_val=", %s" if hasattr(d, "estado") else ""
        )
        params = [d.nombre, d.accion_id, d.tipo_id, d.usuario_id, d.ubicacion_id]
        if hasattr(d, "estado"): params.append(int(d.estado))
        cur.execute(sql, tuple(params))
        self.db.commit()
        new_id = cur.lastrowid
        self.db.close()
        return new_id

    def obtener_por_id(self, id_dispositivo: int) -> Optional[Dispositivo]:
        cur = self.db.get_cursor()
        sql = """SELECT d.ID_DISPOSITIVO, d.NOMBRE_DISPOSITIVO, d.ID_TIPO_DISPOSITIVO, d.ID_USUARIO,
                d.ID_UBICACION, d.ID_ACCION{estado_sel},
                t.NOMBRE_TIPO, u.NOMBRE AS USUARIO_NOMBRE, ub.NOMBRE AS UBICACION_NOMBRE
                FROM DISPOSITIVOS d
                JOIN TIPOSDISPOSITIVO t ON d.ID_TIPO_DISPOSITIVO = t.ID_TIPO_DISPOSITIVO
                JOIN USUARIOS u ON d.ID_USUARIO = u.ID_USUARIO
                JOIN UBICACIONES ub ON d.ID_UBICACION = ub.ID_UBICACION
                WHERE d.ID_DISPOSITIVO=%s""".format(
            estado_sel=", d.ESTADO"
        )
        cur.execute(sql, (id_dispositivo,))
        r = cur.fetchone()
        self.db.close()
        if not r: return None
        return Dispositivo(
            id_dispositivo=r["ID_DISPOSITIVO"],
            nombre=r["NOMBRE_DISPOSITIVO"],
            tipo_id=r["ID_TIPO_DISPOSITIVO"],
            usuario_id=r["ID_USUARIO"],
            ubicacion_id=r["ID_UBICACION"],
            accion_id=r["ID_ACCION"],
            estado=bool(r.get("ESTADO", 0)),
            tipo_nombre=r["NOMBRE_TIPO"],
            ubicacion_nombre=r["UBICACION_NOMBRE"],
        )

    def listar(self, limite=100, offset=0) -> List[Dispositivo]:
        cur = self.db.get_cursor()
        sql = """SELECT d.ID_DISPOSITIVO, d.NOMBRE_DISPOSITIVO, d.ID_TIPO_DISPOSITIVO, d.ID_USUARIO,
                d.ID_UBICACION, d.ID_ACCION{estado_sel},
                t.NOMBRE_TIPO, ub.NOMBRE AS UBICACION_NOMBRE
                FROM DISPOSITIVOS d
                JOIN TIPOSDISPOSITIVO t ON d.ID_TIPO_DISPOSITIVO = t.ID_TIPO_DISPOSITIVO
                JOIN UBICACIONES ub ON d.ID_UBICACION = ub.ID_UBICACION
                ORDER BY d.ID_DISPOSITIVO DESC
                LIMIT %s OFFSET %s""".format(estado_sel=", d.ESTADO")
        cur.execute(sql, (limite, offset))
        rows = cur.fetchall()
        self.db.close()
        return [
            Dispositivo(
                r["ID_DISPOSITIVO"], r["NOMBRE_DISPOSITIVO"], r["ID_TIPO_DISPOSITIVO"],
                r["ID_USUARIO"], r["ID_UBICACION"], r["ID_ACCION"], bool(r.get("ESTADO", 0)),
                r["NOMBRE_TIPO"], r["UBICACION_NOMBRE"]
            ) for r in rows
        ]

    def actualizar(self, d: Dispositivo) -> bool:
        assert d.id_dispositivo is not None
        cur = self.db.get_cursor()
        sql = """UPDATE DISPOSITIVOS
                SET NOMBRE_DISPOSITIVO=%s, ID_ACCION=%s, ID_TIPO_DISPOSITIVO=%s, ID_USUARIO=%s, ID_UBICACION=%s{estado_set}
                WHERE ID_DISPOSITIVO=%s""".format(
            estado_set=", ESTADO=%s"
        )
        params = [d.nombre, d.accion_id, d.tipo_id, d.usuario_id, d.ubicacion_id, int(d.estado), d.id_dispositivo]
        cur.execute(sql, tuple(params))
        self.db.commit()
        ok = cur.rowcount > 0
        self.db.close()
        return ok

    def eliminar(self, id_dispositivo: int) -> bool:
        cur = self.db.get_cursor()
        cur.execute("DELETE FROM DISPOSITIVOS WHERE ID_DISPOSITIVO=%s", (id_dispositivo,))
        self.db.commit()
        ok = cur.rowcount > 0
        self.db.close()
        return ok
