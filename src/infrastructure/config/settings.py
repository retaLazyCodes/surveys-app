from enum import Enum
from pydantic_settings import BaseSettings
import os

class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"

class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True

class Config(BaseConfig):
    DEBUG: int = 1
    DEFAULT_LOCALE: str = "en_US"
    ENVIRONMENT: EnvironmentType = EnvironmentType.DEVELOPMENT
    SQLALCHEMY_DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    RELEASE_VERSION: str = "0.1"
    SHOW_SQL_ALCHEMY_QUERIES: int = 0

config: Config = Config()