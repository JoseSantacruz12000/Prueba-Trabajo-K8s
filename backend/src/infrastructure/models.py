from sqlalchemy import Column, Integer, String
from infrastructure.database import Base

class ClienteORM(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
