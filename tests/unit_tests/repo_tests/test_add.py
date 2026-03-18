"""
Модульные тесты для операций добавления в репозиторий.

Содержит тесты на:
- добавление одного объекта
- добавление множества объектов
- проверку вызова исключений БД
"""

from unittest.mock import MagicMock

import pytest
from asyncpg import UniqueViolationError
from sqlalchemy.exc import IntegrityError
from src.exceptions import ObjectAlreadyExistsException
from src.repositories.base import BaseRepository
from tests.unit_tests.fakes import FakeSchema


@pytest.mark.asyncio
async def test_add_data(
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    """
    Тестирует добавление одного объекта и его возвращение.

    Атрибуты:
    :param mock_repository: репозиторий с замоканным слоем доступа к БД
    :param mock_data: объект схемы после добавления
    """
    result = await mock_repository.add(mock_data)
    assert result == mock_data


@pytest.mark.asyncio
async def test_add_many_data(
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    """
    Тестирует добавление списка объектов и его возвращение.

    Атрибуты:
    :param mock_repository: репозиторий с замоканным слоем доступа к БД
    :param mock_data: объект схемы после добавления
    """
    result = await mock_repository.add_many([mock_data, mock_data])
    assert result == [mock_data, mock_data]


@pytest.mark.parametrize(
    ("cause", "exception"),
    [
        (UniqueViolationError, ObjectAlreadyExistsException),
        (Exception, IntegrityError),
    ],
)
@pytest.mark.asyncio
async def test_add_raise_exceptions(
    mock_repository: BaseRepository,
    mock_execute_scalars: MagicMock,
    mock_data: FakeSchema,
    cause: Exception,
    exception: Exception,
):
    """
    Тестирует вызов исключения для добавления одного объекта.

    Атрибуты:
    :param mock_repository: репозиторий с замоканным слоем доступа к БД
    :param mock_execute_scalars: замоканный результат для имитации поведения БД
    :param mock_data: объект схемы для добавления
    :param cause: ошибка БД
    :param exception: ошибка, которая должна быть выброшена
    """
    mock_execute_scalars.one.side_effect = IntegrityError(
        statement=None, params=None, orig=cause()
    )

    with pytest.raises(exception):
        await mock_repository.add(mock_data)

    # сброс side_effect в None после проверки для предотвращения влияния на другие тесты
    mock_execute_scalars.one.side_effect = None


@pytest.mark.asyncio
async def test_add_many_raise_exceptions(
    mock_execute_scalars: MagicMock,
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    """
    Тестирует вызов исключения для множественного добавления объектов.

    Атрибуты:
    :param mock_repository: репозиторий с замоканным слоем доступа к БД
    :param mock_execute_scalars: замоканный результат для имитации поведения БД
    :param mock_data: объект схемы для добавления
    """
    mock_execute_scalars.all.side_effect = IntegrityError(
        statement=None, params=None, orig=UniqueViolationError()
    )

    with pytest.raises(ObjectAlreadyExistsException):
        await mock_repository.add_many([mock_data, mock_data])

    # сброс side_effect в None после проверки для предотвращения влияния на другие тесты
    mock_execute_scalars.all.side_effect = None
