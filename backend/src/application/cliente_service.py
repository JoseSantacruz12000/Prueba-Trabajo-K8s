from domain.clients import Cliente
from infrastructure.repositories.cliente_repo import ClienteRepository


class ClienteService:
    def __init__(self, repo: ClienteRepository):
        self.repo = repo

    def crear_cliente(self, nombre: str, email: str) -> Cliente:
        cliente = Cliente(id=None, nombre=nombre, email=email)
        return self.repo.save(cliente)

    def listar_clientes(self) -> list[Cliente]:
        return self.repo.find_all()
