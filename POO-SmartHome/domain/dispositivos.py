class Dispositivo:
    def __init__(self, id_dispositivo, tipo, ubicacion, nombre, usuario, estado=2):
        self.__id_dispositivo = id_dispositivo
        self.__tipo = tipo
        self.__ubicacion = ubicacion
        self.__nombre = nombre
        self.__usuario = usuario
        self.__estado = estado

    def get_id_dispositivo(self):
        return self.__id_dispositivo
        
    def get_tipo(self):
        return self.__tipo

    def get_ubicacion(self):
        return self.__ubicacion

    def get_nombre(self):
        return self.__nombre

    def get_usuario(self):
        return self.__usuario
    
    def get_estado(self):
        return self.__estado

    def set_estado(self, nuevo_estado):
        if isinstance(nuevo_estado, int):
            self.__estado = nuevo_estado
        else:
            print("Error: El estado debe ser un valor entero (1. Apagar/2. Encendido).")

class TipoDispositivo: 
    def __init__(self, id_tipo_dispositivo, nombre_tipo, descripcion):
        self.__id_tipo_dispositivo = id_tipo_dispositivo
        self.__nombre_tipo = nombre_tipo
        self.__descripcion = descripcion

    def get_id_tipo_dispositivo(self):
        return self.__id_tipo_dispositivo
    
    def get_nombre_tipo(self):
        return self.__nombre_tipo
    
class Ubicacion:
    def __init__(self, id_ubicacion, nombre, descripcion):
        self.__id_ubicacion = id_ubicacion
        self.__nombre = nombre
        self.__descripcion = descripcion

    def get_id_ubicacion(self):
        return self.__id_ubicacion
    
    def get_nombre(self):
        return self.__nombre