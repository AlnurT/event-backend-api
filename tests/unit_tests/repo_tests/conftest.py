from unittest.mock import AsyncMock, MagicMock

import pytest
from src.repositories.base import BaseRepository
from tests.unit_tests.repo_tests.fakes import FakeDataMapper, FakeORM, FakeSchema


@pytest.fixture(scope="session")
def mock_data() -> FakeSchema:
    return FakeSchema(id=1, name="fake")


@pytest.fixture(scope="session")
def mock_session(mock_data: FakeSchema) -> AsyncMock:
    session = AsyncMock()
    mock_execute = MagicMock()
    session.execute = AsyncMock(return_value=mock_execute)

    mock_scalars = MagicMock()
    mock_execute.scalars.return_value = mock_scalars
    mock_scalars.one.return_value = mock_data
    mock_scalars.all.return_value = [mock_data]

    return session


@pytest.fixture
def mock_execute_scalars(mock_session: AsyncMock) -> MagicMock:
    return mock_session.execute.return_value.scalars.return_value


@pytest.fixture(scope="session")
def mock_repository(mock_session: AsyncMock) -> BaseRepository:
    repository = BaseRepository(mock_session)
    repository.model = FakeORM
    repository.mapper = FakeDataMapper

    return repository
