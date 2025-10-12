from conn.db_conn import ConexionDB
from domain.dispositivos import Dispositivo

class DispositivoDAO:
    def __init__(self):
        self.db = ConexionDB()

    def agregar_dispositivo(self, dispositivo: Dispositivo):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO dispositivos (tipo, ubicacion, nombre, estado) VALUES (%s, %s, %s, %s)"
        valores = (dispositivo.get_tipo(), dispositivo.get_ubicacion(), dispositivo.get_nombre(), dispositivo.get_estado())
        cursor.execute(sql, valores)
        conn.commit()
        print("💡 Dispositivo agregado correctamente.")
