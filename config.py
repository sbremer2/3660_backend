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
    
    database_user: str
    database_password: str
    database_host: str
    database_port: str
    database_name: str
    
    secret_key: str
    algorithm: str
    
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.database_user}:"
            f"{self.database_password}@{self.database_host}:"
            f"{self.database_port}/{self.database_name}"
        )
    
    class Config: 
        env_file = ".env"
        
settings = Settings()