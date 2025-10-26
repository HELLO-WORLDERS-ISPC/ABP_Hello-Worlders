import unittest
from unittest.mock import patch, MagicMock
from dao.dispositivos_dao import DispositivoDAO

class FakeDispositivo:
    def __init__(self, id_dispositivo, tipo, ubicacion, nombre, usuario, estado=1):
        self.__id_dispositivo = id_dispositivo
        self.__tipo = tipo
        self.__ubicacion = ubicacion
        self.__nombre = nombre
        self.__usuario = usuario
        self.__estado = estado

    def get_tipo(self): return self.__tipo
    def get_ubicacion(self): return self.__ubicacion
    def get_nombre(self): return self.__nombre
    def get_usuario(self): return self.__usuario
    def get_estado(self): return self.__estado

class TestDispositivoDAO(unittest.TestCase):
    def setUp(self):
        patcher = patch('dao.dispositivos_dao.ConexionDB')
        self.mock_db = patcher.start()
        self.addCleanup(patcher.stop)

        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor
        self.mock_db.return_value.get_connection.return_value = self.mock_conn

        self.dao = DispositivoDAO()

    def test_insert_dispositivo_commit(self):
        disp = FakeDispositivo(1, 1, 1, 'Sensor', 'User', 1)
        self.dao.agregar_dispositivo(disp)
        self.mock_cursor.execute.assert_called_once()
        sql, params = self.mock_cursor.execute.call_args[0]
        self.assertIn('INSERT INTO DISPOSITIVOS', sql.upper())
        self.assertEqual(len(params), 5)
        self.mock_conn.commit.assert_called_once()

    def test_listar_dispositivos_devuelve_lista(self):
        self.mock_cursor.fetchall.return_value = [
            {'ID_DISPOSITIVO': 1, 'NOMBRE': 'Sensor', 'USUARIO': 'User'}
        ]
        dispositivos = self.dao.listar_todos_dispositivos()
        self.assertIsInstance(dispositivos, list)
        self.assertGreaterEqual(len(dispositivos), 1)

