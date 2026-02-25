from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base, str_50, str_500


class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(str_50, unique=True)
    name: Mapped[str] = mapped_column(str_50)
    age: Mapped[int]
    phone_number: Mapped[str] = mapped_column(String(20))
    player_level: Mapped[str]
    description: Mapped[str] = mapped_column(str_500, nullable=True)
