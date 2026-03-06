from unittest.mock import AsyncMock, MagicMock

import pytest
from src.repositories.base import BaseRepository
from tests.unit_tests.repo_tests.fakes import FakeDataMapper, FakeORM, FakeSchema


@pytest.fixture(scope="session")
def mock_session() -> AsyncMock:
    session = AsyncMock()
    mock_execute = MagicMock()
    mock_scalars = MagicMock()

    mock_execute.scalars.return_value = mock_scalars
    session.execute.return_value = mock_execute

    return session


@pytest.fixture(scope="session")
def mock_execute_scalars(mock_session: AsyncMock) -> MagicMock:
    return mock_session.execute.return_value.scalars.return_value


def mock_session_execute_return_value(
    mock_session: AsyncMock,
    data: list[FakeSchema],
) -> None:
    mock_session.execute.return_value.scalars.return_value.all.return_value = data


@pytest.fixture(scope="session")
def mock_repository(mock_session: AsyncMock) -> BaseRepository:
    repository = BaseRepository(mock_session)
    repository.model = FakeORM
    repository.mapper = FakeDataMapper

    return repository
