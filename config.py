from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_env: str
    allow_origins: list[AnyHttpUrl]
    cloudinary_cloud_name: str
    cloudinary_api_key: str
    cloudinary_api_secret: str
    pexels_api_key: str
    api_token: str
    
    class Config: 
        env_file = ".env"
        
settings = Settings()