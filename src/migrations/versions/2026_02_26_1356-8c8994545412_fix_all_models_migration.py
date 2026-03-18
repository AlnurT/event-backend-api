"""fix all models migration

Revision ID: 8c8994545412
Revises: 5d7c8fa27b2c
Create Date: 2026-02-26 13:56:38.731771

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "8c8994545412"
down_revision: str | Sequence[str] | None = "5d7c8fa27b2c"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "events", sa.Column("event_name", sa.String(length=50), nullable=False)
    )
    op.add_column("events", sa.Column("min_event_level", sa.String(), nullable=False))
    op.alter_column(
        "events", "description", existing_type=sa.VARCHAR(length=500), nullable=True
    )
    op.drop_column("events", "game_level")
    op.drop_column("events", "events_name")
    op.add_column("records", sa.Column("user_id", sa.Integer(), nullable=False))
    op.drop_constraint(op.f("records_player_id_fkey"), "records", type_="foreignkey")
    op.create_foreign_key(None, "records", "users", ["user_id"], ["id"])
    op.drop_column("records", "player_id")
    op.add_column("reviews", sa.Column("user_id", sa.Integer(), nullable=False))
    op.add_column("reviews", sa.Column("review_data", sa.Date(), nullable=False))
    op.add_column(
        "reviews", sa.Column("review_text", sa.String(length=500), nullable=True)
    )
    op.drop_constraint(op.f("reviews_player_id_fkey"), "reviews", type_="foreignkey")
    op.create_foreign_key(None, "reviews", "users", ["user_id"], ["id"])
    op.drop_column("reviews", "review_time")
    op.drop_column("reviews", "player_id")
    op.drop_column("reviews", "review")
    op.add_column("users", sa.Column("user_level", sa.String(), nullable=False))
    op.drop_column("users", "player_level")


def downgrade() -> None:
    """Downgrade schema."""
    op.add_column(
        "users",
        sa.Column("player_level", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_column("users", "user_level")
    op.add_column(
        "reviews",
        sa.Column("review", sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    )
    op.add_column(
        "reviews",
        sa.Column("player_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "reviews",
        sa.Column(
            "review_time", postgresql.TIMESTAMP(), autoincrement=False, nullable=False
        ),
    )
    op.drop_constraint(None, "reviews", type_="foreignkey")
    op.create_foreign_key(
        op.f("reviews_player_id_fkey"), "reviews", "users", ["player_id"], ["id"]
    )
    op.drop_column("reviews", "review_text")
    op.drop_column("reviews", "review_data")
    op.drop_column("reviews", "user_id")
    op.add_column(
        "records",
        sa.Column("player_id", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(None, "records", type_="foreignkey")
    op.create_foreign_key(
        op.f("records_player_id_fkey"), "records", "users", ["player_id"], ["id"]
    )
    op.drop_column("records", "user_id")
    op.add_column(
        "events",
        sa.Column(
            "events_name", sa.VARCHAR(length=200), autoincrement=False, nullable=False
        ),
    )
    op.add_column(
        "events",
        sa.Column("game_level", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.alter_column(
        "events", "description", existing_type=sa.VARCHAR(length=500), nullable=False
    )
    op.drop_column("events", "min_event_level")
    op.drop_column("events", "event_name")
