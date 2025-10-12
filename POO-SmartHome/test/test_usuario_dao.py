import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import unittest
from unittest.mock import MagicMock, patch
from dao.usuarios_dao import UsuarioDAO

class FakeUsuario:
    def __init__(self, id_usuario, email, nombre, login, clave, rol_nombre=None, rol_id=None):
        self._id = id_usuario
        self._email = email
        self._nombre = nombre
        self._login = login
        self._rol_nombre = rol_nombre
        self._rol_id = rol_id
        setattr(self, "_Usuario__clave", clave)

    def get_login(self): return self._login
    def get_email(self): return self._email
    def get_nombre(self): return self._nombre
    def get_rol(self):   return self._rol_id if self._rol_id else self._rol_nombre


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
        u = FakeUsuario(None, "a@b.com", "Alice", "alice", "hash123", rol_id=2)

        self.dao.registrar(u)

        self.mock_conn.cursor.assert_called_once_with()
        self.mock_cursor.execute.assert_called_once()
        sql, params = self.mock_cursor.execute.call_args[0]
        self.assertIn("INSERT INTO usuarios", sql)
        self.assertEqual(params, ("alice", "a@b.com", "Alice", "hash123", 2))
        self.mock_conn.commit.assert_called_once()

    def test_login_correcto_retorna_usuario(self):
        def cursor_factory(**kwargs):
            return self.mock_cursor
        self.mock_conn.cursor.side_effect = cursor_factory

        self.mock_cursor.fetchone.return_value = {
            "ID_USUARIO": 1, "EMAIL": "a@b.com", "NOMBRE": "Alice",
            "USUARIO": "alice", "CLAVE": "123", "NOMBRE_ROL": "ADMIN"
        }

        with patch('dao.usuarios_dao.Usuario', FakeUsuario):
            user = self.dao.login("alice", "123")

        self.assertIsInstance(user, FakeUsuario)
        self.assertEqual(user._login, "alice")
        self.assertEqual(user._rol_nombre, "ADMIN")

    def test_login_contraseña_incorrecta_devuelve_none(self):
        def cursor_factory(**kwargs):
            return self.mock_cursor
        self.mock_conn.cursor.side_effect = cursor_factory
        self.mock_cursor.fetchone.return_value = {
            "ID_USUARIO": 1, "EMAIL": "a@b.com", "NOMBRE": "Alice",
            "USUARIO": "alice", "CLAVE": "hash123", "NOMBRE_ROL": "ADMIN"
        }

        user = self.dao.login("alice", "otra")
        self.assertIsNone(user)

    def test_cambiar_rol_hace_update_y_commit(self):
        self.dao.cambiar_rol(5, 2)
        self.mock_conn.cursor.assert_called_once_with()
        self.mock_cursor.execute.assert_called_once()
        sql, params = self.mock_cursor.execute.call_args[0]
        self.assertIn("UPDATE USUARIOS", sql.upper())
        self.assertEqual(params, (2, 5))
        self.mock_conn.commit.assert_called_once()

    def test_listar_todos_usuarios_devuelve_lista(self):
        def cursor_factory(**kwargs):
            return self.mock_cursor
        self.mock_conn.cursor.side_effect = cursor_factory
        self.mock_cursor.fetchall.return_value = [
            {"ID_USUARIO": 1, "USUARIO": "alice", "NOMBRE_USUARIO": "Alice", "EMAIL": "a@b.com", "NOMBRE_ROL": "ADMIN"},
            {"ID_USUARIO": 2, "USUARIO": "bob", "NOMBRE_USUARIO": "Bob", "EMAIL": "b@b.com", "NOMBRE_ROL": "INVITADO"},
        ]

        with patch('dao.usuarios_dao.Usuario', FakeUsuario):
            usuarios = self.dao.listar_todos_usuarios()

        self.assertEqual(len(usuarios), 2)
        self.assertIsInstance(usuarios[0], FakeUsuario)
        self.assertEqual(usuarios[0]._login, "alice")

    def test_existe_email_true_y_false(self):
        self.mock_cursor.fetchone.return_value = (1,)
        self.assertTrue(self.dao.existe_email("a@b.com"))
        self.mock_cursor.fetchone.return_value = (0,)
        self.assertFalse(self.dao.existe_email("x@y.com"))

if __name__ == "__main__":
    unittest.main()
