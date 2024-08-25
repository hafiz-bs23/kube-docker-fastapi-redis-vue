import pydantic_settings
class Settings(pydantic_settings.BaseSettings):
    origins: list = ["http://localhost", "http://localhost:8080"]
    
    
settings = Settings()