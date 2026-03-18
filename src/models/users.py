"""
Модуль содержит ORM-модель участников для работы с таблицей users.

Содержит определение полей и их назначение в контексте базы данных.
"""

from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base, str_50, str_500


class UsersOrm(Base):
    """
    ORM-модель участников.

     Поля:
    - id (int): первичный ключ.
    - email (str): почта (не более 50 символов, уникальная).
    - name (str): имя (не более 50 символов).
    - description (str | None): о себе.
    """

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(str_50, unique=True)
    name: Mapped[str] = mapped_column(str_50)
    description: Mapped[str | None] = mapped_column(str_500, nullable=True)
