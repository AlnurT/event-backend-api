"""
Модуль содержит ORM-модель отзывов для работы с таблицей reviews.

Содержит определение полей и их назначение в контексте базы данных.
"""

from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base, str_500


class ReviewsOrm(Base):
    """
    ORM-модель отзывов.

     Поля:
    - id (int): первичный ключ.
    - user_id (int): внешний ключ на участника (users.id).
    - event_id (int): внешний ключ на мероприятие (events.id).
    - review_data (date): дата отзыва.
    - review_text (str | None): отзыв.
    """

    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    review_data: Mapped[date]
    review_text: Mapped[str | None] = mapped_column(str_500, nullable=True)
