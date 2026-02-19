from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base, str_200, str_500


class EventsOrm(Base):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True)
    organizer_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    events_name: Mapped[str] = mapped_column(str_200)
    description: Mapped[str] = mapped_column(str_500)
    game_level: Mapped[int] = mapped_column(default=0)
