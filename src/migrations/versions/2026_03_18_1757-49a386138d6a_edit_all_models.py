"""edit all models

Revision ID: 49a386138d6a
Revises: 8c8994545412
Create Date: 2026-03-18 17:57:27.167222

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "49a386138d6a"
down_revision: str | Sequence[str] | None = "8c8994545412"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.drop_column("events", "min_event_level")
    op.drop_column("reviews", "event_rating")
    op.drop_column("users", "phone_number")
    op.drop_column("users", "user_level")
    op.drop_column("users", "age")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "users", sa.Column("age", sa.INTEGER(), autoincrement=False, nullable=False)
    )
    op.add_column(
        "users",
        sa.Column("user_level", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "users",
        sa.Column(
            "phone_number", sa.VARCHAR(length=20), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "reviews",
        sa.Column("event_rating", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "events",
        sa.Column("min_event_level", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
