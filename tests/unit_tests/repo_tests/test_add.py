from unittest.mock import MagicMock

import pytest
from asyncpg import UniqueViolationError
from sqlalchemy.exc import IntegrityError
from src.exceptions import ObjectAlreadyExistsException
from src.repositories.base import BaseRepository
from tests.unit_tests.repo_tests.fakes import FakeSchema


@pytest.mark.asyncio
async def test_add_data(
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    result = await mock_repository.add(mock_data)
    assert result == mock_data


@pytest.mark.asyncio
async def test_add_many_data(
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    result = await mock_repository.add_many([mock_data])
    assert result == [mock_data]


@pytest.mark.parametrize(
    ("cause", "exception"),
    [
        (UniqueViolationError, ObjectAlreadyExistsException),
        (Exception, IntegrityError),
    ],
)
@pytest.mark.asyncio
async def test_add_raise_exceptions(
    mock_execute_scalars: MagicMock,
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
    cause: Exception,
    exception: Exception,
):
    mock_execute_scalars.one.side_effect = IntegrityError(
        statement=None, params=None, orig=cause()
    )

    with pytest.raises(exception):
        await mock_repository.add(mock_data)

    mock_execute_scalars.one.side_effect = None


@pytest.mark.asyncio
async def test_add_many_raise_exceptions(
    mock_execute_scalars: MagicMock,
    mock_repository: BaseRepository,
    mock_data: FakeSchema,
):
    mock_execute_scalars.all.side_effect = IntegrityError(
        statement=None, params=None, orig=UniqueViolationError()
    )

    with pytest.raises(ObjectAlreadyExistsException):
        await mock_repository.add_many([mock_data])

    mock_execute_scalars.all.side_effect = None
