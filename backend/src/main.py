from fastapi import FastAPI
from infrastructure.database import Base, engine
from infrastructure import models
from interfaces.api import cliente_router

# Crear tablas automáticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pedido Backend con FastAPI 🚀")

app.include_router(cliente_router.router)

@app.get("/")
def root():
    return {"message": "API de pedidos funcionando con PostgreSQL"}
