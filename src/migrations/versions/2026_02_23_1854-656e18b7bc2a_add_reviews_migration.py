"""add reviews migration

Revision ID: 656e18b7bc2a
Revises: 00fc3a8871d5
Create Date: 2026-02-23 18:54:31.137544

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "656e18b7bc2a"
down_revision: str | Sequence[str] | None = "00fc3a8871d5"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "reviews",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("player_id", sa.Integer(), nullable=False),
        sa.Column("event_id", sa.Integer(), nullable=False),
        sa.Column("review_time", sa.DateTime(), nullable=False),
        sa.Column("event_rating", sa.Integer(), nullable=False),
        sa.Column("review", sa.String(length=500), nullable=True),
        sa.ForeignKeyConstraint(
            ["event_id"],
            ["events.id"],
        ),
        sa.ForeignKeyConstraint(
            ["player_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("reviews")
