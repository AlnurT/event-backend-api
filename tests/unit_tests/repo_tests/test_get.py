"""
Модульные тесты для операций получения из репозитория.

Содержит тесты на:
- получения всех объектов
- получения отфильтрованных объектов
"""

from unittest.mock import MagicMock

import pytest
from src.repositories.base import BaseRepository
from tests.unit_tests.fakes import FakeSchema


@pytest.mark.asyncio
async def test_get_all_data(
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    """
    Тестирует получение объектов.

    Атрибуты:
    :param mock_repository: репозиторий с замоканным слоем доступа к БД
    :param mock_data: объект схемы после получения
    """
    result = await mock_repository.get_all()
    assert result == [mock_data, mock_data]


@pytest.mark.asyncio
async def test_get_filtered_data(
    mock_repository: BaseRepository,
    mock_execute_scalars: MagicMock,
    mock_data: FakeSchema,
):
    """
    Тестирует получение отфильтрованного объекта.

    Атрибуты:
    :param mock_repository: репозиторий с замоканным слоем доступа к БД
    :param mock_execute_scalars: замоканный результат для имитации поведения БД
    :param mock_data: объект схемы после получения
    """
    mock_execute_scalars.all.return_value = [mock_data]

    result = await mock_repository.get_filtered(name="fake")
    assert result == [mock_data]

    # возврат значения после проверки для предотвращения влияния на другие тесты
    mock_execute_scalars.all.return_value = [mock_data, mock_data]
