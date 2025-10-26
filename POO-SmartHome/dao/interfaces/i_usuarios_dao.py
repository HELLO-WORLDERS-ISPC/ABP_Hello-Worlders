from abc import ABC, abstractmethod
from typing import List, Optional
import re

from domain.usuarios import Usuario


class IUsuarioDAO(ABC):
    @abstractmethod
    def registrar(self, usuario: str) -> None:
        pass

    @abstractmethod
    def login(self, login: str, clave: str) -> Optional[Usuario]:
        pass

    @abstractmethod
    def cambiar_rol(self, id_usuario: int, nuevo_rol: int) -> None:
        pass

    @abstractmethod
    def listar_todos_usuarios(self) -> List[Usuario]:
        pass

    @abstractmethod
    def existe_email(self, email: str) -> bool:
        pass

    @abstractmethod
    def es_email_valido(self, email: str) -> Optional[re.Match]:
        pass
