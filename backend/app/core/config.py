from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CineMatch"
    PROJECT_VERSION: str = "0.1.0"
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str
    TMDB_API_KEY: str
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

