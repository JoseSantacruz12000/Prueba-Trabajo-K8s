import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_USER: str = os.getenv("DB_USER", "admin")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "supersecret")
    DB_HOST: str = os.getenv("DB_HOST", "pedido-app-postgresql")
    DB_NAME: str = os.getenv("DB_NAME", "pedidos")

    class Config:
        env_file = ".env"

settings = Settings()
