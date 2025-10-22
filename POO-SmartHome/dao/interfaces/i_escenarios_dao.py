from abc import ABC, abstractmethod
from domain.escenarios import Escenario


class IEscenarioDAO(ABC):
    @abstractmethod
    def crear_escenario(self, escenario: Escenario) -> None:
        pass
