"""
Фикстуры для юнит-тестов.

 Этот модуль содержит:
- фикстуры, возвращающие тестовые данные.
- асинхронная имитация сессии SQLAlchemy.
- вспомогательная фикстура `mock_execute_scalars`, возвращающая объект scalars().
"""

from unittest.mock import AsyncMock, MagicMock

import pytest
from src.repositories.base import BaseRepository
from tests.unit_tests.fakes import FakeDataMapper, FakeORM, FakeSchema


@pytest.fixture(scope="session")
def mock_data() -> FakeSchema:
    """
    Возвращает фиксированный объект данных в виде pydantic-схемы для тестов.
    """
    return FakeSchema(id=1, name="fake")


@pytest.fixture(scope="session")
def mock_session(mock_data: FakeSchema) -> AsyncMock:
    """
    Создаёт имитацию асинхронной сессии SQLAlchemy.

     Поведение:
    - session.execute возвращает объект mock_execute (AsyncMock-обёртка).
    - mock_execute.scalars().one() возвращает `mock_data`.
    - mock_execute.scalars().all() возвращает список из одного элемента `mock_data`.

    Эта фикстура удобна для тестирования методов репозиториев, которые выполняют
    запросы и затем извлекают одиночный результат через scalars().one() или несколько
    результатов через scalars().all().

    :return: session (AsyncMock) - имитация сессии.
    """
    session = AsyncMock()
    mock_execute = MagicMock()
    session.execute = AsyncMock(return_value=mock_execute)

    mock_scalars = MagicMock()
    mock_execute.scalars.return_value = mock_scalars
    mock_scalars.one.return_value = mock_data
    mock_scalars.all.return_value = [mock_data, mock_data]

    return session


@pytest.fixture
def mock_execute_scalars(mock_session: AsyncMock) -> MagicMock:
    """
    Возвращает объект, который имитирует результат вызова execute().scalars().

    Это позволяет в тестах напрямую настраивать поведение scalars (например,
    переопределить return_value.one или return_value.all) без перенастройки всей сессии.
    """
    return mock_session.execute.return_value.scalars.return_value


@pytest.fixture(scope="session")
def mock_repository(mock_session: AsyncMock) -> BaseRepository:
    """
    Создаёт и возвращает экземпляр BaseRepository, настроенный для тестов.

     Поведение:
    - Конструктор получает `mock_session` вместо реальной сессии БД.
    - Устанавливаются `model` и `mapper` для работы с тестовой моделью `FakeORM`
      и маппером `FakeDataMapper`.

    Эта фикстура используется в тестах репозиториев, чтобы вызывать методы CRUD
    и проверять их поведение с предсказуемыми mock-ответами.

    :return: repository (BaseRepository) - тестовый репозиторий.
    """
    repository = BaseRepository(mock_session)
    repository.model = FakeORM
    repository.mapper = FakeDataMapper

    return repository
