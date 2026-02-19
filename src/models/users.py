from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base, str_200, str_500


class UsersOrm(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column(str_200, unique=True)
    hashed_password: Mapped[str] = mapped_column(str_200)
    name: Mapped[str] = mapped_column(str_200)

    role: Mapped[str] = mapped_column(str_200, nullable=True)
    description: Mapped[str] = mapped_column(str_500, nullable=True)
    photo_url: Mapped[str | None] = mapped_column(str_500, nullable=True)
    age: Mapped[int | None] = mapped_column(nullable=True)
    phone_number: Mapped[str | None] = mapped_column(String(20), nullable=True)
    player_level: Mapped[int] = mapped_column(default=0)
