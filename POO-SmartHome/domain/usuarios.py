from dataclasses import dataclass
from typing import Optional

@dataclass
class Usuario:
    id_usuario: Optional[int]
    login: str
    nombre: str
    clave: str
    rol_id: int            
    email: Optional[str] = None


