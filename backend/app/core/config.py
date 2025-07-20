from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    """
    Carrega as configurações do projeto a partir de um arquivo .env.
    """
    PROJECT_NAME: str
    PROJECT_VERSION: str
    SECRET_KEY: str

    class Config:
        # O Pydantic procurará por um arquivo .env na mesma pasta ou em pastas superiores
        # e o carregará.
        env_file = ".env"
        env_file_encoding = 'utf-8' # Adicionado para garantir a codificação correta

# Cria uma instância única das configurações que será usada em todo o projeto.
settings = Settings()

