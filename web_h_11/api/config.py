import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Settings class to handle configuration using environment variables.
    """
    DATABASE_URL: str
    TEST_DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    CLOUDINARY_URL: str
    REDIS_URL: str

    class Config:
        """
        Configuration class for settings.
        """
        env_file = ".env"

settings = Settings()


