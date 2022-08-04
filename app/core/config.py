from typing import Dict, Optional

from pydantic import BaseSettings, PostgresDsn, validator

from dotenv import load_dotenv


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"

    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_DESCRIPTION: str

    POSTGRES_SERVER: Optional[str]
    POSTGRES_USER: Optional[str]
    POSTGRES_PASSWORD: Optional[str]
    POSTGRES_DB: Optional[str]
    SQLALCHEMY_DATABASE_URI: str

    class Config:
        case_sensitive = True


def get_settings():
    load_dotenv()
    return Settings()


settings = get_settings()
