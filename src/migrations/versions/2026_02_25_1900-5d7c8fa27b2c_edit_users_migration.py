"""edit users migration

Revision ID: 5d7c8fa27b2c
Revises: 656e18b7bc2a
Create Date: 2026-02-25 19:00:47.699738

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "5d7c8fa27b2c"
down_revision: str | Sequence[str] | None = "656e18b7bc2a"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""

    op.alter_column(
        "users",
        "email",
        existing_type=sa.VARCHAR(length=200),
        type_=sa.String(length=50),
        existing_nullable=False,
    )
    op.alter_column(
        "users",
        "name",
        existing_type=sa.VARCHAR(length=200),
        type_=sa.String(length=50),
        existing_nullable=False,
    )
    op.alter_column("users", "age", existing_type=sa.INTEGER(), nullable=False)
    op.alter_column(
        "users", "phone_number", existing_type=sa.VARCHAR(length=20), nullable=False
    )
    op.alter_column(
        "users",
        "player_level",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
    )
    op.drop_column("users", "hashed_password")
    op.drop_column("users", "role")
    op.drop_column("users", "photo_url")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "users",
        sa.Column(
            "photo_url", sa.VARCHAR(length=500), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "users",
        sa.Column("role", sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    )
    op.add_column(
        "users",
        sa.Column(
            "hashed_password",
            sa.VARCHAR(length=200),
            autoincrement=False,
            nullable=False,
        ),
    )
    op.alter_column(
        "users",
        "player_level",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )
    op.alter_column(
        "users", "phone_number", existing_type=sa.VARCHAR(length=20), nullable=True
    )
    op.alter_column("users", "age", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column(
        "users",
        "name",
        existing_type=sa.String(length=50),
        type_=sa.VARCHAR(length=200),
        existing_nullable=False,
    )
    op.alter_column(
        "users",
        "email",
        existing_type=sa.String(length=50),
        type_=sa.VARCHAR(length=200),
        existing_nullable=False,
    )
