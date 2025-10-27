from conn.db_conn import ConexionDB
from domain.dispositivos import Dispositivo, TipoDispositivo, Ubicacion
from dao.interfaces.i_dispositivos_dao import IDispositivoDAO

class DispositivoDAO(IDispositivoDAO):
    def __init__(self):
        self.db = ConexionDB()

    def agregar_dispositivo(self, dispositivo: Dispositivo):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO dispositivos (ID_TIPO_DISPOSITIVO, ID_UBICACION, NOMBRE_DISPOSITIVO, ID_USUARIO, ID_ACCION) VALUES (%s, %s, %s, %s, %s)"
        valores = (dispositivo.get_tipo(), dispositivo.get_ubicacion(), dispositivo.get_nombre(), dispositivo.get_usuario(), dispositivo.get_estado())
        cursor.execute(sql, valores)
        conn.commit()
        print("Dispositivo agregado correctamente")

    def listar_tipos_dispositivo(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """SELECT  
                t.ID_TIPO_DISPOSITIVO,
                t.NOMBRE_TIPO,
                t.DESCRIPCION
                FROM TIPOSDISPOSITIVO t"""
        cursor.execute(sql)
        resultados = cursor.fetchall()
        tipos_dispositivo = []

        for row in resultados:
            tipos_dispositivo.append(TipoDispositivo(row['ID_TIPO_DISPOSITIVO'],row['NOMBRE_TIPO'], row['DESCRIPCION']))

        return tipos_dispositivo
    
    def listar_ubicaciones(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """SELECT  
                u.ID_UBICACION,
                u.NOMBRE,
                u.DESCRIPCION
                FROM UBICACIONES u"""
        cursor.execute(sql)
        resultados = cursor.fetchall()
        ubicaciones = []

        for row in resultados:
            ubicaciones.append(Ubicacion(row['ID_UBICACION'],row['NOMBRE'], row['DESCRIPCION']))

        return ubicaciones
     
    def listar_todos_dispositivos(self):
        conn = self.db.get_connection()
        cursor = conn.cursor(dictionary=True)
        sql = """
            SELECT 
                d.ID_DISPOSITIVO,
                t.NOMBRE_TIPO AS TIPO,
                ub.NOMBRE AS UBICACION,
                d.NOMBRE_DISPOSITIVO AS NOMBRE,
                u.NOMBRE AS USUARIO,
                a.ACCION_DETALLE AS ESTADO
            FROM DISPOSITIVOS d
            JOIN TIPOSDISPOSITIVO t ON d.ID_TIPO_DISPOSITIVO = t.ID_TIPO_DISPOSITIVO
            JOIN UBICACIONES ub ON d.ID_UBICACION = ub.ID_UBICACION
            JOIN USUARIOS u ON d.ID_USUARIO = u.ID_USUARIO
            JOIN ESTADODISPOSITIVO a ON d.ID_ACCION = a.ID_ACCION 
            ORDER BY ID_DISPOSITIVO ASC;
        """
        cursor.execute(sql)
        resultados = cursor.fetchall()
        cursor.close()

        dispositivos = []
        for row in resultados:
            dispositivos.append(
                Dispositivo(
                    row['ID_DISPOSITIVO'],
                    row['TIPO'],
                    row['UBICACION'],
                    row['NOMBRE'],
                    row['USUARIO'],
                    row['ESTADO']
                )
            )

        return dispositivos

    
    def editar_estado_dispositivo(self, id_dispositivo, nuevo_estado):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "UPDATE dispositivos SET ID_ACCION = %s WHERE ID_DISPOSITIVO = %s"
        cursor.execute(sql, (nuevo_estado, id_dispositivo))
        conn.commit()
        cursor.close()
        print("Estado del dispositivo actualizado correctamente")
    
    def eliminar_dispositivo(self, id_dispositivo):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM dispositivos WHERE ID_DISPOSITIVO = %s"
        cursor.execute(sql, (id_dispositivo,))
        conn.commit()
        cursor.close()
        print("Dispositivo eliminado correctamente")