from unittest.mock import AsyncMock

import pytest
from src.exceptions import ObjectNotFoundException
from src.repositories.base import BaseRepository
from tests.unit_tests.repo_tests.conftest import mock_session_execute_return_value
from tests.unit_tests.repo_tests.fakes import FakeSchema


@pytest.mark.parametrize(
    "data",
    [
        [FakeSchema(id=1, name="fake")],
        [],
    ],
)
@pytest.mark.asyncio
async def test_get_all_data(
    mock_session: AsyncMock,
    mock_repository: BaseRepository,
    data: list[FakeSchema],
):
    mock_session_execute_return_value(mock_session, data)
    result = await mock_repository.get_all()

    assert result == data
    mock_session.execute.assert_called()


@pytest.mark.parametrize(
    ("name_filter", "data"),
    [
        ("fake", [FakeSchema(id=1, name="fake")]),
        ("nonexistent", []),
    ],
)
@pytest.mark.asyncio
async def test_get_filtered_data(
    mock_session: AsyncMock,
    mock_repository: BaseRepository,
    name_filter: str,
    data: list[FakeSchema],
):
    mock_session_execute_return_value(mock_session, data)
    result = await mock_repository.get_filtered(name=name_filter)

    assert result == data
    mock_session.execute.assert_called()


@pytest.mark.asyncio
async def test_raise_exception(
    mock_session: AsyncMock,
    mock_repository: BaseRepository,
):
    mock_session.execute.side_effect = ObjectNotFoundException

    with pytest.raises(ObjectNotFoundException):
        await mock_repository.get_filtered()
