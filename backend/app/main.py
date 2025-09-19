# Localização: backend/app/main.py

from fastapi import FastAPI
from fastapi.security import HTTPBearer # Mantenha esta importação (apesar de não a usar diretamente no app, é boa prática para indicar intenção)
from app.core.config import settings

# --- Configuração da Base de Dados ---
from app.db.base import Base # Certifique-se que é app.db.base
from app.db.session import engine

# --- Roteadores ---
from app.api.routes import users, movies

# --- Criação das Tabelas ---
Base.metadata.create_all(bind=engine)

# --- Criação da Aplicação ---
app = FastAPI(
    title=settings.PROJECT_NAME,
    # Você pode querer adicionar um `version` no config.py e usá-lo aqui, ex: version=settings.PROJECT_VERSION
    # openapi_tags é opcional, mas ajuda a organizar a documentação
    openapi_tags=[
        {
            "name": "users",
            "description": "Operations with users.",
        },
        {
            "name": "movies",
            "description": "Operations with movies.",
        },
    ],
    # openapi_extra é a chave para forçar o Swagger UI a mostrar a opção "Bearer"
    openapi_extra={
        "security": [{"Bearer": []}], # Indica que as rotas esperam um esquema de segurança chamado "Bearer"
        "components": {
            "securitySchemes": {
                "Bearer": { # Define o esquema de segurança "Bearer"
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                    "description": "JWT Authorization header using the Bearer scheme. Example: 'Bearer {token}'"
                }
            }
        }
    }
)

# --- Inclusão dos Roteadores ---
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(movies.router, prefix="/movies", tags=["movies"])

@app.get("/")
def read_root():
    """Endpoint raiz para verificar se a API está online."""
    return {"message": "Bem-vindo ao CineMatch API!"}