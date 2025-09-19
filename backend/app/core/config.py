from pydantic_settings import BaseSettings

class Settings(BaseSettings):
   
    PROJECT_NAME: str = "CineMatch"
    PROJECT_VERSION: str = "0.1.0"
    
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  
    TMDB_API_KEY : str

    DATABASE_URL: str 

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8' 

settings = Settings()

