from sqlalchemy.orm import Session
from infrastructure import models
from domain.clients import Cliente
from infrastructure.database import SessionLocal

class ClienteRepository:
    def __init__(self, db: Session = SessionLocal()):
        self.db = db

    def save(self, cliente: Cliente) -> Cliente:
        orm_cliente = models.ClienteORM(nombre=cliente.nombre, email=cliente.email)
        self.db.add(orm_cliente)
        self.db.commit()
        self.db.refresh(orm_cliente)
        return Cliente(id=orm_cliente.id, nombre=orm_cliente.nombre, email=orm_cliente.email)

    def find_all(self) -> list[Cliente]:
        clientes = self.db.query(models.ClienteORM).all()
        return [Cliente(id=c.id, nombre=c.nombre, email=c.email) for c in clientes]
