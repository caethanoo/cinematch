# Localização: backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.core.config import settings

# --- Configuração da Base de Dados ---
from app.db.base import Base # Certifique-se que é app.db.base
from app.db.session import engine

# --- Roteadores ---
from app.api.routes import users, movies

# --- Criação das Tabelas ---
Base.metadata.create_all(bind=engine)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        description="API do CineMatch",
        routes=app.routes,
    )
    
    # Definindo o esquema de segurança JWT
    openapi_schema["components"]["securitySchemes"] = {
        "Bearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
            "description": "Digite seu token JWT"
        }
    }
    
    # Aplicando segurança globalmente
    openapi_schema["security"] = [{"Bearer": []}]
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

# --- Criação da Aplicação ---
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="API para o aplicativo CineMatch",
    openapi_tags=[
        {"name": "users", "description": "Operações com usuários"},
        {"name": "movies", "description": "Operações com filmes"},
    ]
)

# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Atribuindo o schema personalizado
app.openapi = custom_openapi

# --- Inclusão dos Roteadores ---
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(movies.router, prefix="/movies", tags=["movies"])

@app.get("/")
def read_root():
    """Endpoint raiz para verificar se a API está online."""
    return {"message": "Bem-vindo ao CineMatch API!"}