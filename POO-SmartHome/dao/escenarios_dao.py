from conn.db_conn import ConexionDB
from domain.escenarios import Escenario
from dao.interfaces.i_escenarios_dao import IEscenarioDAO

class EscenarioDAO(IEscenarioDAO):
    def __init__(self):
        self.db = ConexionDB()

    def crear_escenario(self, escenario: Escenario):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO escenarios (nombre, descripcion) VALUES (%s, %s)"
        cursor.execute(sql, (escenario.get_nombre(), escenario.get_descripcion()))
        conn.commit()
        print("Escenario creado correctamente")
