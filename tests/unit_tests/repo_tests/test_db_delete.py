from unittest.mock import MagicMock

import pytest
from sqlalchemy.exc import NoResultFound
from src.exceptions import ObjectNotFoundException
from src.repositories.base import BaseRepository
from tests.unit_tests.repo_tests.fakes import FakeSchema


@pytest.mark.asyncio
async def test_delete_data(
    mock_execute_scalars: MagicMock,
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    result = await mock_repository.delete(id=1)
    assert result == mock_data


@pytest.mark.asyncio
async def test_delete_raise_exceptions(
    mock_execute_scalars: MagicMock,
    mock_repository: BaseRepository,
):
    mock_execute_scalars.one.side_effect = NoResultFound

    with pytest.raises(ObjectNotFoundException):
        await mock_repository.delete(id=2)

    mock_execute_scalars.one.side_effect = None
