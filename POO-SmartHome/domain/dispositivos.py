from dataclasses import dataclass
from typing import Optional

@dataclass
class Dispositivo:
    id_dispositivo: Optional[int]
    nombre: str
    tipo_id: int
    usuario_id: int
    ubicacion_id: int
    accion_id: Optional[int]
    estado: bool = False