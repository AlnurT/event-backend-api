"""add users migration

Revision ID: 3b0a0f14ee3b
Revises:
Create Date: 2026-02-18 19:22:36.983201

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "3b0a0f14ee3b"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=200), nullable=False),
        sa.Column("hashed_password", sa.String(length=200), nullable=False),
        sa.Column("name", sa.String(length=200), nullable=False),
        sa.Column("role", sa.String(length=200), nullable=False),
        sa.Column("photo_url", sa.String(length=500), nullable=True),
        sa.Column("age", sa.Integer(), nullable=True),
        sa.Column("phone_number", sa.String(length=20), nullable=True),
        sa.Column("player_level", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("users")
