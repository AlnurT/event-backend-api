from unittest.mock import MagicMock

import pytest
from asyncpg import UniqueViolationError
from sqlalchemy.exc import IntegrityError
from src.exceptions import ObjectAlreadyExistsException
from src.repositories.base import BaseRepository
from tests.unit_tests.repo_tests.fakes import FakeSchema


@pytest.mark.asyncio
async def test_add_data(
    mock_execute_scalars: MagicMock,
    mock_repository: BaseRepository,
):
    data = FakeSchema(id=1, name="fake")
    mock_execute_scalars.one.return_value = data
    result = await mock_repository.add(data)
    assert result == data


@pytest.mark.parametrize(
    ("cause", "exception"),
    [
        (UniqueViolationError, ObjectAlreadyExistsException),
        (Exception, IntegrityError),
    ],
)
@pytest.mark.asyncio
async def test_raise_exceptions(
    mock_execute_scalars: MagicMock,
    mock_repository: BaseRepository,
    cause: Exception,
    exception: Exception,
):
    data = FakeSchema(id=1, name="fake")
    mock_execute_scalars.one.side_effect = IntegrityError(
        statement=None, params=None, orig=cause()
    )

    with pytest.raises(exception):
        await mock_repository.add(data)
