import pytest
from src.repositories.base import BaseRepository
from tests.unit_tests.repo_tests.fakes import FakeSchema


@pytest.mark.asyncio
async def test_get_all_data(
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    result = await mock_repository.get_all()

    assert result == [mock_data]


@pytest.mark.asyncio
async def test_get_filtered_data(
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    result = await mock_repository.get_filtered(name="fake")

    assert result == [mock_data]
