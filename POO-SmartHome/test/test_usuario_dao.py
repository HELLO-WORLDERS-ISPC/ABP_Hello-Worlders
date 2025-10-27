import unittest
from unittest.mock import patch, MagicMock
from dao.usuarios_dao import UsuarioDAO

class FakeUsuario:
    def __init__(self, id_usuario, email, nombre, login, clave, rol=2):
        self.__id_usuario = id_usuario
        self.__email = email
        self.__nombre = nombre
        self.__login = login
        self._Usuario__clave = clave
        self.__rol = rol

    def get_login(self): return self.__login
    def get_email(self): return self.__email
    def get_nombre(self): return self.__nombre
    def get_rol(self): return self.__rol

class TestUsuarioDAO(unittest.TestCase):
    def setUp(self):
        patcher = patch('dao.usuarios_dao.ConexionDB')
        self.mock_db_class = patcher.start()
        self.addCleanup(patcher.stop)

        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor
        self.mock_db_class.return_value.get_connection.return_value = self.mock_conn

        self.dao = UsuarioDAO()

    def test_registrar_inserta_y_commit(self):
        usuario = FakeUsuario(1, 'test@mail.com', 'Test User', 'testuser', '1234', 2)
        self.dao.registrar(usuario)
        self.mock_cursor.execute.assert_called_once()
        sql, params = self.mock_cursor.execute.call_args[0]
        self.assertIn('INSERT INTO USUARIOS', sql.upper())
        self.assertEqual(len(params), 5)
        self.mock_conn.commit.assert_called_once()

    def test_cambiar_rol_y_commit(self):
        self.dao.cambiar_rol(1, 2)
        self.mock_cursor.execute.assert_called_once()
        sql, params = self.mock_cursor.execute.call_args[0]
        self.assertIn('UPDATE USUARIOS', sql.upper())
        self.mock_conn.commit.assert_called_once()

    def test_listar_todos_devuelve_lista(self):
        self.mock_cursor.fetchall.return_value = [
            {'ID_USUARIO': 1, 'EMAIL': 'a@mail.com', 'NOMBRE_USUARIO': 'A', 'USUARIO': 'a', 'NOMBRE_ROL': 'admin'}
        ]
        usuarios = self.dao.listar_todos_usuarios()
        self.assertIsInstance(usuarios, list)
        self.assertEqual(len(usuarios), 1)
        self.mock_cursor.execute.assert_called_once()

    def test_existe_email_true_false(self):
        self.mock_cursor.fetchone.side_effect = [(1,), (0,)]
        self.assertTrue(self.dao.existe_email('x@mail.com'))
        self.assertFalse(self.dao.existe_email('y@mail.com'))


