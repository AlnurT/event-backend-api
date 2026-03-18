"""add events migration

Revision ID: 54c279010b6e
Revises: 3b0a0f14ee3b
Create Date: 2026-02-19 13:42:30.680862

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "54c279010b6e"
down_revision: str | Sequence[str] | None = "3b0a0f14ee3b"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("organizer_id", sa.Integer(), nullable=False),
        sa.Column("events_name", sa.String(length=200), nullable=False),
        sa.Column("description", sa.String(length=500), nullable=False),
        sa.Column("game_level", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["organizer_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.add_column(
        "users", sa.Column("description", sa.String(length=500), nullable=True)
    )
    op.alter_column(
        "users", "role", existing_type=sa.VARCHAR(length=200), nullable=True
    )
    op.alter_column("users", "player_level", existing_type=sa.INTEGER(), nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column("users", "player_level", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column(
        "users", "role", existing_type=sa.VARCHAR(length=200), nullable=False
    )
    op.drop_column("users", "description")
    op.drop_table("events")
