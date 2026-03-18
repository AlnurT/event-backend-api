"""
Тесты, проверяющие наличие таблиц моделей в тестовой базе данных.

Тесты используют вспомогательную функцию `get_tables` для извлечения
списка таблиц через SQLAlchemy `inspect`.
"""

import pytest
from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import AsyncEngine
from src.database import engine_null_pool


async def get_tables(async_engine: AsyncEngine):
    """
    Получает список таблиц из базы данных.

     Параметры:
    - async_engine (AsyncEngine): асинхронный SQLAlchemy-движок для подключения.

    :return: list[str]: список имён таблиц в схеме, видимых через inspect.
    """
    async with async_engine.connect() as conn:
        tables = await conn.run_sync(
            lambda sync_conn: inspect(sync_conn).get_table_names()
        )
        return tables


@pytest.mark.parametrize(
    "model_name",
    ["users", "events", "records", "reviews", "fakes"],
)
@pytest.mark.asyncio
async def test_models_exist(model_name: str):
    """
    Проверяет, что таблица для заданной модели существует в схеме.
    """
    tables = await get_tables(engine_null_pool)
    assert model_name in tables


@pytest.mark.asyncio
async def test_model_not_exist():
    """
    Проверяет, что в базе данных ровно ожидаемое количество таблиц
    и что несуществующая таблица `other` отсутствует.
    """
    tables = await get_tables(engine_null_pool)
    assert len(tables) == 5
    assert "other" not in tables
