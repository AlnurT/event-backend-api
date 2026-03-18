"""
Фикстуры и начальная конфигурация для тестов.

Этот модуль предоставляет фикстуры для работы с БД в тестах и использует движок
без пула соединений.
"""

import pytest
from src.config import settings
from src.database import Base, async_session_null_pool, engine_null_pool
from src.models import *  # noqa: F403
from src.utils.db_manager import DBManager


@pytest.fixture(scope="session", autouse=True)
def check_test_mode():
    """
    Проверяет, что приложение запущено в тестовом режиме.

    - scope: session - инициализация будет выполнена один раз при запуске всех тестов.
    - autouse: True - выполняется автоматически для всей сессии тестов.
    """
    assert settings.MODE == "TEST"


async def get_db_null_pool() -> DBManager:
    """
    Асинхронный генератор, предоставляющий экземпляр DBManager,
    используется внутри фикстур для обеспечения корректного закрытия/очистки
    соединений после использования.
    """
    async with DBManager(session_factory=async_session_null_pool) as db:
        yield db


@pytest.fixture(autouse=True)
async def db() -> DBManager:
    """
    Фикстура, предоставляющая объект DBManager для каждого теста.

    - autouse: True - автоматически доступна во всех тестах.
    Является обёрткой вокруг `get_db_null_pool` и просто делегирует
    генераторное значение.
    """
    async for db in get_db_null_pool():
        yield db


@pytest.fixture(scope="session", autouse=True)
async def setup_database(check_test_mode):
    """
    Инициализация БД перед запуском тестовой сессии.

    - scope: session - инициализация будет выполнена один раз при запуске всех тестов.
    - autouse: True - выполняется автоматически для всей сессии тестов.

     Поведение:
    - Подключается к `engine_null_pool`.
    - Удаляет все таблицы и затем создаёт их заново, чтобы обеспечить чистую
      и предсказуемую схему для тестов.
    """
    async with engine_null_pool.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
