"""
Тестовые вспомогательные классы.

Этот модуль содержит простую ORM-модель `FakeORM`, соответствующую тестовой таблице
`fakes`, Pydantic-схему `FakeSchema` и маппер `FakeDataMapper`, используемые
в тестах для проверки поведения CRUD-операций без привязки к реальным моделям.
"""

from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from src.repositories.mappers.base import DataMapper


class FakeORM(Base):
    """
    Простая ORM-модель для таблицы тестовых данных.

     Поля:
    - id (int): первичный ключ.
    - name (str): название.
    """

    __tablename__ = "fakes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class FakeSchema(BaseModel):
    """
    Pydantic-схема для тестовых данных.

     Атрибуты:
    - id (int): id.
    - name (str): название.
    """

    id: int
    name: str


class FakeDataMapper(DataMapper):
    """
    Конкретизация базового `DataMapper` для тестовой модели.

     Атрибуты:
    - db_model: ORM-класс `FakeORM`.
    - schema: Pydantic-схема `FakeSchema`.

    Используется в тестах для проверки корректности
    операций преобразования между ORM-объектами и схемами.
    """

    db_model = FakeORM
    schema = FakeSchema
