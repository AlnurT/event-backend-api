import pytest
from src.config import settings
from src.database import Base, async_session_null_pool, engine_null_pool
from src.models import *  # noqa: F403
from src.utils.db_manager import DBManager


@pytest.fixture(scope="session", autouse=True)
def check_test_mode():
    assert settings.MODE == "TEST"


async def get_db_null_pool() -> DBManager:
    async with DBManager(session_factory=async_session_null_pool) as db:
        yield db


@pytest.fixture(autouse=True)
async def db() -> DBManager:
    async for db in get_db_null_pool():
        yield db


@pytest.fixture(scope="session", autouse=True)
async def setup_database(check_test_mode):
    async with engine_null_pool.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
