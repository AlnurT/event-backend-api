from unittest.mock import MagicMock

import pytest
from sqlalchemy.exc import IntegrityError
from src.exceptions import ObjectNotFoundException
from src.repositories.base import BaseRepository
from tests.unit_tests.repo_tests.fakes import FakeSchema


@pytest.mark.asyncio
async def test_edit_data(
    mock_execute_scalars: MagicMock,
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    result = await mock_repository.edit(mock_data, id=1)
    assert result == mock_data


@pytest.mark.asyncio
async def test_edit_raise_exceptions(
    mock_execute_scalars: MagicMock,
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    mock_execute_scalars.one.side_effect = IntegrityError(
        statement=None, params=None, orig=Exception
    )

    with pytest.raises(ObjectNotFoundException):
        await mock_repository.edit(mock_data, id=2)

    mock_execute_scalars.one.side_effect = None
