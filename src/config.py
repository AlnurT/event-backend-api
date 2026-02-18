from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MODE: Literal["LOCAL", "TEST"]

    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DB_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parent.parent / ".env")
    )


settings = Settings()
