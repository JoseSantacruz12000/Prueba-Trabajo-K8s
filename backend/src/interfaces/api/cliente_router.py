from fastapi import APIRouter, Depends
from application.cliente_service import ClienteService
from infrastructure.repositories.cliente_repo import ClienteRepository

router = APIRouter(prefix="/clientes", tags=["clientes"])

def get_service():
    repo = ClienteRepository()
    return ClienteService(repo)

@router.post("/home")
def crear_cliente(nombre: str, email: str, service: ClienteService = Depends(get_service)):
    return service.crear_cliente(nombre, email)

@router.get("/home")
def listar_clientes(service: ClienteService = Depends(get_service)):
    return service.listar_clientes()
