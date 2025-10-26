import mysql.connector

class ConexionDB:
    def __init__(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="R00t",
                database="smart_home"
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos MySQL.")
        except mysql.connector.Error as error:
            print(f"Error al conectar a la base de datos: {error}")

    def get_cursor(self):
        return self.connection.cursor()
    
    def get_connection(self):  
        return self.connection

    def commit(self):
        self.connection.commit()

    def close(self):
        if self.connection.is_connected():
            self.connection.close()
            print("🔌 Conexión cerrada correctamente.")
