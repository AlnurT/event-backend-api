"""
Пакет моделей приложения.

Этот модуль позволяет создавать миграции с помощью Alembic.
В нем определены все модели, которые используются в приложении
и будут отображаться в базе данных.
"""

from src.models.events import EventsOrm
from src.models.records import RecordsOrm
from src.models.reviews import ReviewsOrm
from src.models.users import UsersOrm

__all__ = [
    "EventsOrm",
    "RecordsOrm",
    "ReviewsOrm",
    "UsersOrm",
]
