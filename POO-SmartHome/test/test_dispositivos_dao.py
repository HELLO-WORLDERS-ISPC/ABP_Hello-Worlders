import unittest
from unittest.mock import MagicMock, patch
from dao.dispositivos_dao import DispositivoDAO

class FakeDispositivo:
    def __init__(self, id, tipo, ubicacion, nombre, usuario, estado):
        self._id = id
        self._tipo = tipo
        self._ubicacion = ubicacion
        self._nombre = nombre
        self._usuario = usuario
        self._estado = estado
    def get_tipo(self): return self._tipo
    def get_ubicacion(self): return self._ubicacion
    def get_nombre(self): return self._nombre
    def get_usuario(self): return self._usuario
    def get_estado(self): return self._estado

class FakeTipoDispositivo:
    def __init__(self, id, nombre, descripcion):
        self.id=id; self.nombre=nombre; self.descripcion=descripcion

class FakeUbicacion:
    def __init__(self, id, nombre, descripcion):
        self.id=id; self.nombre=nombre; self.descripcion=descripcion

class TestDispositivoDAO(unittest.TestCase):
    def setUp(self):
        patcher = patch('dao.dispositivos_dao.ConexionDB')
        self.mock_db_class = patcher.start()
        self.addCleanup(patcher.stop)
        self.mock_conn = MagicMock()
        self.mock_cursor = MagicMock()
        self.mock_conn.cursor.return_value = self.mock_cursor
        self.mock_db_class.return_value.get_connection.return_value = self.mock_conn
        self.dao = DispositivoDAO()

    def test_agregar_dispositivo_inserta_y_commit(self):
        d = FakeDispositivo(1, 2, 3, "Lampara", 4, 1)
        self.dao.agregar_dispositivo(d)
        self.mock_cursor.execute.assert_called_once()
        sql, params = self.mock_cursor.execute.call_args[0]
        self.assertIn("INSERT INTO dispositivos", sql)
        self.assertEqual(params, (2, 3, "Lampara", 4, 1))
        self.mock_conn.commit.assert_called_once()

    def test_listar_tipos_dispositivo_retorna_lista(self):
        def cursor_factory(**kwargs): return self.mock_cursor
        self.mock_conn.cursor.side_effect = cursor_factory
        self.mock_cursor.fetchall.return_value = [
            {"ID_TIPO_DISPOSITIVO":1,"NOMBRE_TIPO":"Luz","DESCRIPCION":"Iluminación"},
            {"ID_TIPO_DISPOSITIVO":2,"NOMBRE_TIPO":"Cámara","DESCRIPCION":"Seguridad"}
        ]
        with patch('dao.dispositivos_dao.TipoDispositivo', FakeTipoDispositivo):
            tipos = self.dao.listar_tipos_dispositivo()
        self.assertEqual(len(tipos),2)
        self.assertIsInstance(tipos[0], FakeTipoDispositivo)
        self.assertEqual(tipos[0].nombre,"Luz")

    def test_listar_ubicaciones_retorna_lista(self):
        def cursor_factory(**kwargs): return self.mock_cursor
        self.mock_conn.cursor.side_effect = cursor_factory
        self.mock_cursor.fetchall.return_value = [
            {"ID_UBICACION":1,"NOMBRE":"Living","DESCRIPCION":"Principal"},
            {"ID_UBICACION":2,"NOMBRE":"Cocina","DESCRIPCION":"Preparación"}
        ]
        with patch('dao.dispositivos_dao.Ubicacion', FakeUbicacion):
            ubicaciones = self.dao.listar_ubicaciones()
        self.assertEqual(len(ubicaciones),2)
        self.assertIsInstance(ubicaciones[1], FakeUbicacion)
        self.assertEqual(ubicaciones[1].nombre,"Cocina")

    def test_listar_todos_dispositivos_retorna_lista(self):
        def cursor_factory(**kwargs): return self.mock_cursor
        self.mock_conn.cursor.side_effect = cursor_factory
        self.mock_cursor.fetchall.return_value = [
            {"ID_DISPOSITIVO":1,"TIPO":"Luz","UBICACION":"Living","NOMBRE":"Lampara","USUARIO":"Facu","ESTADO":"Encendido"},
            {"ID_DISPOSITIVO":2,"TIPO":"Camara","UBICACION":"Cocina","NOMBRE":"Cam","USUARIO":"Ana","ESTADO":"Apagado"}
        ]
        with patch('dao.dispositivos_dao.Dispositivo', FakeDispositivo):
            dispositivos = self.dao.listar_todos_dispositivos()
        self.assertEqual(len(dispositivos),2)
        self.assertIsInstance(dispositivos[0], FakeDispositivo)
        self.assertEqual(dispositivos[0]._nombre,"Lampara")

    def test_editar_estado_dispositivo_update_y_commit(self):
        self.dao.editar_estado_dispositivo(10,5)
        self.mock_cursor.execute.assert_called_once()
        sql,params=self.mock_cursor.execute.call_args[0]
        self.assertIn("UPDATE dispositivos", sql)
        self.assertEqual(params,(5,10))
        self.mock_conn.commit.assert_called_once()

    def test_eliminar_dispositivo_delete_y_commit(self):
        self.dao.eliminar_dispositivo(7)
        self.mock_cursor.execute.assert_called_once()
        sql,params=self.mock_cursor.execute.call_args[0]
        self.assertIn("DELETE FROM dispositivos", sql)
        self.assertEqual(params,(7,))
        self.mock_conn.commit.assert_called_once()

if __name__ == "__main__":
    unittest.main()
