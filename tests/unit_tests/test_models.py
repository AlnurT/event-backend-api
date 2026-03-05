import pytest
from src.database import engine_null_pool
from tests.conftest import get_tables


@pytest.mark.parametrize(
    ("model_name", "is_in_db"),
    [
        ("users", True),
        ("events", True),
        ("records", True),
        ("reviews", True),
        ("fakes", True),
        ("other", False),
    ],
)
async def test_model_exists(
    model_name: str,
    is_in_db: bool,
):
    tables = await get_tables(engine_null_pool)
    assert (model_name in tables) == is_in_db
