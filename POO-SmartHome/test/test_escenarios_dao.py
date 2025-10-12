import unittest
from unittest.mock import MagicMock, patch
from dao.escenarios_dao import EscenarioDAO

class FakeEscenario:
    def __init__(self, id, nombre, descripcion):
        self._id=id; self._nombre=nombre; self._descripcion=descripcion
    def get_nombre(self): return self._nombre
    def get_descripcion(self): return self._descripcion

class TestEscenarioDAO(unittest.TestCase):
    def setUp(self):
        patcher = patch('dao.escenarios_dao.ConexionDB')
        self.mock_db_class = patcher.start()
        self.addCleanup(patcher.stop)
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor
        self.mock_db_class.return_value.get_connection.return_value = self.mock_conn
        self.dao = EscenarioDAO()

    def test_crear_escenario_inserta_y_commit(self):
        e = FakeEscenario(1,"Modo Noche","Apaga luces y cierra persianas")
        self.dao.crear_escenario(e)
        self.mock_cursor.execute.assert_called_once()
        sql,params=self.mock_cursor.execute.call_args[0]
        self.assertIn("INSERT INTO escenarios",sql)
        self.assertEqual(params,("Modo Noche","Apaga luces y cierra persianas"))
        self.mock_conn.commit.assert_called_once()

if __name__=="__main__":
    unittest.main()
