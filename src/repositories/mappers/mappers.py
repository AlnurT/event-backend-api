"""Конкретные реализации мапперов данных (DataMapper).

Модуль содержит подклассы DataMapper, которые связывают конкретные
ORM-модели (SQLAlchemy) с соответствующими Pydantic-схемами.
Каждый класс предоставляет атрибуты db_model и schema, указывающие
на модель БД и схему для валидации/сериализации соответственно.
"""

from src.models import EventsOrm, RecordsOrm, ReviewsOrm, UsersOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.events import EventSchema
from src.schemas.records import RecordSchema
from src.schemas.reviews import ReviewSchema
from src.schemas.users import UserSchema


class UserDataMapper(DataMapper):
    """
    DataMapper для пользователей.

     Атрибуты:
    - db_model (UsersOrm): ORM-модель.
    - schema (UserSchema): Pydantic-схема.
    """

    db_model = UsersOrm
    schema = UserSchema


class EventDataMapper(DataMapper):
    """
    DataMapper для событий.

     Атрибуты:
    - db_model (EventsOrm): ORM-модель.
    - schema (EventSchema): Pydantic-схема.
    """

    db_model = EventsOrm
    schema = EventSchema


class RecordDataMapper(DataMapper):
    """
    DataMapper для записей.

     Атрибуты:
    - db_model (RecordsOrm): ORM-модель.
    - schema (RecordSchema): Pydantic-схема.
    """

    db_model = RecordsOrm
    schema = RecordSchema


class ReviewDataMapper(DataMapper):
    """
    DataMapper для отзывов.

     Атрибуты:
    - db_model (ReviewsOrm): ORM-модель.
    - schema (ReviewSchema): Pydantic-схема.
    """

    db_model = ReviewsOrm
    schema = ReviewSchema
