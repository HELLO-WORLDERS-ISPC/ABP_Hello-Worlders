import unittest
from unittest.mock import patch, MagicMock
from dao.escenarios_dao import EscenarioDAO

class FakeEscenario:
    def __init__(self, id_escenario, nombre, descripcion=""):
        self.__id_escenario = id_escenario
        self.__nombre = nombre
        self.__descripcion = descripcion

    def get_nombre(self): return self.__nombre
    def get_descripcion(self): return self.__descripcion

class TestEscenarioDAO(unittest.TestCase):
    def setUp(self):
        patcher = patch('dao.escenarios_dao.ConexionDB')
        self.mock_db = patcher.start()
        self.addCleanup(patcher.stop)

        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor
        self.mock_db.return_value.get_connection.return_value = self.mock_conn

        self.dao = EscenarioDAO()

    def test_insert_escenario_commit(self):
        esc = FakeEscenario(1, 'Escena', 'Desc')
        self.dao.crear_escenario(esc)
        self.mock_cursor.execute.assert_called_once()
        sql, params = self.mock_cursor.execute.call_args[0]
        self.assertIn('INSERT INTO ESCENARIOS', sql.upper())
        self.assertEqual(len(params), 2)
        self.mock_conn.commit.assert_called_once()


