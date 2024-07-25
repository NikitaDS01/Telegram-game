import os
from pydantic import SecretStr
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict

class Config(BaseSettings):
    TOKEN: SecretStr
    ALLOWED_UPDATES: SecretStr
    DATABASE_URL: SecretStr

    model_config = SettingsConfigDict(
        env_file=os.path.join(os.path.dirname(__file__), ".env"),
        env_file_encoding="utf-8"
    )

config = Config()