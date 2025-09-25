# Localização: backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.core.config import settings
# >>> NOVAS IMPORTAÇÕES NECESSÁRIAS PARA A CONFIGURAÇÃO DO SWAGGER UI <<<
from fastapi.openapi.docs import get_swagger_ui_html # Adicione esta linha
from fastapi.security import OAuth2PasswordBearer # Adicione esta linha
from starlette.responses import HTMLResponse # Adicione esta linha (FastAPI usa Starlette)


# --- Configuração da Base de Dados ---
from app.db.base import Base
from app.db.session import engine

# Criar tabelas
Base.metadata.create_all(bind=engine)

# >>> ADICIONE ESTA LINHA: Define onde o Swagger UI deve ir buscar o token <<<
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/token")


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=settings.PROJECT_NAME,
        version=settings.PROJECT_VERSION,
        description="API para o aplicativo CineMatch",
        routes=app.routes,
    )

    # ... (restante da sua definição de openapi_schema) ...

    # Aplicando segurança globalmente
    openapi_schema["security"] = [{"bearerAuth": []}] # Isso está correto para a documentação

    app.openapi_schema = openapi_schema
    return app.openapi_schema

# Criar aplicação
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="API para o aplicativo CineMatch",
    # >>> ADICIONE ESTA CONFIGURAÇÃO PARA O COMPORTAMENTO DO SWAGGER UI <<<
    # AQUI É ONDE DIZEMOS AO SWAGGER UI COMO INTERAGIR COM O FLUXO DE TOKEN
    swagger_ui_init_oauth={
        "usePkceWithAuthorizationCodeGrant": True, # Ajuda a simplificar
        "clientId": "swagger-ui-client", # Um ID de cliente genérico
        "scopes": "openid profile email", # Escopos genéricos
        "tokenUrl": "/users/token" # O URL do seu endpoint de token
    }
)

# >>> CONFIGURAÇÃO PERSONALIZADA DO SWAGGER UI PARA INCLUIR O ESQUEMA BEARER <<<
# Esta função irá gerar a página HTML do Swagger UI
def get_swagger_ui_with_bearer_oauth():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        init_oauth=app.swagger_ui_init_oauth,
        # ESTA É A PARTE CRÍTICA QUE DIZ AO SWAGGER UI SOBRE O ESQUEMA DE SEGURANÇA INTERATIVO
        swagger_ui_parameters={
            "bearerAuth": { # O nome aqui deve corresponder ao do securitySchemes no custom_openapi
                "type": "apiKey",
                "name": "Authorization",
                "in": "header"
            }
        },
        swagger_ui_init_kwargs={
            "security_schemes": {
                "bearerAuth": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                    "description": "JWT Authorization header using the Bearer scheme."
                }
            }
        }
    )

# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Atribuir o schema personalizado
app.openapi = custom_openapi

# >>> SUBSTITUA A ROTA DEFAULT /docs PELA NOSSA VERSÃO CUSTOMIZADA <<<
@app.get("/docs", include_in_schema=False, response_class=HTMLResponse)
async def custom_swagger_ui():
    return get_swagger_ui_with_bearer_oauth()


# Importar e incluir routers
from app.api.routes import users, movies, swipes

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(movies.router, prefix="/movies", tags=["movies"])
app.include_router(swipes.router, prefix="/swipes", tags=["swipes"])

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao CineMatch API!"}