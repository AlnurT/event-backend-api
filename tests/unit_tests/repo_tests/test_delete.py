"""
Модульные тесты для операций удаления из репозитория.

Содержит тесты на:
- удаление объекта
- проверку вызова исключения БД
"""

from unittest.mock import MagicMock

import pytest
from sqlalchemy.exc import NoResultFound
from src.exceptions import ObjectNotFoundException
from src.repositories.base import BaseRepository
from tests.unit_tests.fakes import FakeSchema


@pytest.mark.asyncio
async def test_delete_data(
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    """
    Тестирует удаления объекта и его возвращение.

    Атрибуты:
    :param mock_repository: репозиторий с замоканным слоем доступа к БД
    :param mock_data: объект схемы после удаления
    """
    result = await mock_repository.delete(id=1)
    assert result == mock_data


@pytest.mark.asyncio
async def test_delete_raise_exceptions(
    mock_repository: BaseRepository,
    mock_execute_scalars: MagicMock,
):
    """
    Тестирует вызов исключения для удаления объекта.

    Атрибуты:
    :param mock_repository: репозиторий с замоканным слоем доступа к БД
    :param mock_execute_scalars: замоканный результат для имитации поведения БД
    """
    mock_execute_scalars.one.side_effect = NoResultFound

    with pytest.raises(ObjectNotFoundException):
        await mock_repository.delete(id=2)

    # сброс side_effect в None после проверки для предотвращения влияния на другие тесты
    mock_execute_scalars.one.side_effect = None
