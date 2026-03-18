"""
Модуль содержит ORM-модель мероприятий для работы с таблицей events.

Содержит определение полей и их назначение в контексте базы данных.
"""

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base, str_50, str_500


class EventsOrm(Base):
    """
    ORM-модель мероприятий.

     Поля:
    - id (int): первичный ключ.
    - organizer_id (int): внешний ключ на организатора (users.id).
    - event_name (str): название мероприятия (не более 50 символов).
    - description (str | None): описание мероприятия
      (необязательное поле, не более 500 символов).
    """

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    organizer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    event_name: Mapped[str] = mapped_column(str_50)
    description: Mapped[str | None] = mapped_column(str_500, nullable=True)
