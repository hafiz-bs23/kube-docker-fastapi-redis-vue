from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    origins: list = ["http://localhost", "http://localhost:8080"]
    
settings = Settings()