from abc import ABC, abstractmethod
from typing import List
from domain.dispositivos import Dispositivo, TipoDispositivo, Ubicacion


class IDispositivoDAO(ABC):
    @abstractmethod
    def agregar_dispositivo(self, dispositivo: Dispositivo) -> None:
        pass

    @abstractmethod
    def listar_tipos_dispositivo(self) -> List[TipoDispositivo]:
        pass

    @abstractmethod
    def listar_ubicaciones(self) -> List[Ubicacion]:
        pass

    @abstractmethod
    def listar_todos_dispositivos(self) -> List[Dispositivo]:
        pass

    @abstractmethod
    def editar_estado_dispositivo(self, id_dispositivo: int, nuevo_estado: int) -> None:
        pass

    @abstractmethod
    def eliminar_dispositivo(self, id_dispositivo: int) -> None:
        pass
