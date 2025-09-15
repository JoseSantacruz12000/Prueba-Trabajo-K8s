from dataclasses import dataclass

@dataclass
class Cliente:
    id: int | None
    nombre: str
    email: str
