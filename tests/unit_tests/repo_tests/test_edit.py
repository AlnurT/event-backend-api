"""
Модульные тесты для операций изменения в репозитории.

Содержит тесты на:
- изменение объекта
- проверку вызова исключения БД
"""

from unittest.mock import MagicMock

import pytest
from sqlalchemy.exc import IntegrityError
from src.exceptions import ObjectNotFoundException
from src.repositories.base import BaseRepository
from tests.unit_tests.fakes import FakeSchema


@pytest.mark.asyncio
async def test_edit_data(
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    """
    Тестирует изменение объекта и его возвращение.

    Атрибуты:
    :param mock_repository: репозиторий с замоканным слоем доступа к БД
    :param mock_data: объект схемы после изменения
    """
    result = await mock_repository.edit(mock_data, id=1)
    assert result == mock_data


@pytest.mark.asyncio
async def test_edit_raise_exceptions(
    mock_repository: BaseRepository,
    mock_execute_scalars: MagicMock,
    mock_data: FakeSchema,
):
    """
    Тестирует вызов исключения для изменения объекта.

    Атрибуты:
    :param mock_repository: репозиторий с замоканным слоем доступа к БД
    :param mock_execute_scalars: замоканный результат для имитации поведения БД
    :param mock_data: объект схемы для изменения
    """
    mock_execute_scalars.one.side_effect = IntegrityError(
        statement=None, params=None, orig=Exception
    )

    with pytest.raises(ObjectNotFoundException):
        await mock_repository.edit(mock_data, id=2)

    # сброс side_effect в None после проверки для предотвращения влияния на другие тесты
    mock_execute_scalars.one.side_effect = None
