from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base, str_50, str_500


class EventsOrm(Base):
    """Модель мероприятий в БД"""

    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    organizer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    event_name: Mapped[str] = mapped_column(str_50)
    min_event_level: Mapped[str]
    description: Mapped[str | None] = mapped_column(str_500, nullable=True)
