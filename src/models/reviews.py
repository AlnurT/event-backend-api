from datetime import date

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base, str_500


class ReviewsOrm(Base):
    """Модель отзывов мероприятий в БД"""

    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    event_id: Mapped[int] = mapped_column(ForeignKey("events.id"))
    review_data: Mapped[date]
    event_rating: Mapped[int]
    review_text: Mapped[str | None] = mapped_column(str_500, nullable=True)
