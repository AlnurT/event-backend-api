"""
Модуль конфигурации приложения.

Содержит Pydantic-совместимый класс Settings, который загружает значения
из файла .env, собирает параметры подключения к базе данных и режим работы
приложения.
"""

from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Настройки приложения для работы с базой данных PostgreSQL.

     Атрибуты:
    - MODE (Literal["LOCAL", "TEST"]): режим работы - локальная разработка,
      тестирование.
    - DB_HOST (str): хост сервера БД.
    - DB_PORT (int): порт сервера БД.
    - DB_USER (str): имя пользователя БД.
    - DB_PASS (str): пароль пользователя БД.
    - DB_NAME (str): название БД.

     Свойства:
    - DB_URL (str): асинхронное подключение к БД.
    """

    # Режим работы приложения
    MODE: Literal["LOCAL", "TEST"]

    # Параметры подключения к БД
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DB_URL(self) -> str:
        """
        Формирует строку подключения к PostgreSQL через asyncpg для SQLAlchemy.

        Возвращаемая строка имеет формат:
            postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}
        """
        return (
            f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )

    # Указание файла .env расположенного на уровень выше каталога src
    model_config = SettingsConfigDict(
        env_file=str(Path(__file__).parent.parent / ".env")
    )


settings = Settings()
