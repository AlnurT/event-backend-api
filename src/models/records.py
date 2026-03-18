"""
Модуль содержит ORM-модель записей для работы с таблицей records.

Содержит определение полей и их назначение в контексте базы данных.
"""

from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base


class RecordsOrm(Base):
    """
    ORM-модель записей.

     Поля:
    - id (int): первичный ключ.
    - user_id (int): внешний ключ на участника (users.id).
    - event_id (int): внешний ключ на событие (events.id).
    - datetime_from (datetime): дата и время начала мероприятия.
    - datetime_to (datetime): дата и время конца мероприятия.
    """

    __tablename__ = "records"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    datetime_from: Mapped[datetime]
    datetime_to: Mapped[datetime]
