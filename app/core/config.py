from typing import Any, Dict, List, Optional, Union
from pydantic_settings import SettingsConfigDict, BaseSettings
from pydantic import AnyHttpUrl, validator, field_validator, ValidationInfo
import os


class Settings(BaseSettings):
    model_config = SettingsConfigDict(extra='allow', env_file=".env", case_sensitive=True)

    _ROOT_PATH: str = os.path.abspath(os.path.curdir)
    _CORE_PATH: str = os.path.abspath(os.path.dirname(__file__))

    PROJECT_NAME: str

    SMTP_USERNAME: Optional[str] = None
    SMTP_PASSWORD: Optional[str] = None
    SMTP_HOST: Optional[str] = None
    SMTP_PORT: Optional[int] = None

    JWT_SECRET: Optional[str] = None
    JWT_ALGORITHM: Optional[str] = None

    # 60 minutes * 24 hours * 3 days = 3 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 3

    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    
    @field_validator("BACKEND_CORS_ORIGINS", mode='before')
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[AnyHttpUrl]:
        if isinstance(v, str) and not v.startswith("["):
            return [AnyHttpUrl(origin.strip()) for origin in v.split(",")]
        elif isinstance(v, (list, str)):
            return [AnyHttpUrl(x.strip()) for x in v]
        raise ValueError(v)

    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: int
    MYSQL_DATABASE: str

    DATABASE_URI: Optional[str] = None

    @field_validator('DATABASE_URI', mode='before')
    @classmethod
    def assemble_db_sync_connection(cls, v: str, info: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        return f"mysql://{info.data['MYSQL_USER']}:{info.data['MYSQL_PASSWORD']}@{info.data['MYSQL_HOST']}:{info.data['MYSQL_PORT']}/{info.data['MYSQL_DATABASE']}"
    
    DATABASE_URIX: Optional[str] = None

    @field_validator('DATABASE_URIX', mode='before')
    @classmethod
    def assemble_db_async_connection(cls, v: str, info: ValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        return f"mysql+aiomysql://{info.data['MYSQL_USER']}:{info.data['MYSQL_PASSWORD']}@{info.data['MYSQL_HOST']}:{info.data['MYSQL_PORT']}/{info.data['MYSQL_DATABASE']}"

settings = Settings()
