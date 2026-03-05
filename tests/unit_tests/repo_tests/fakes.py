from pydantic import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from src.database import Base
from src.repositories.mappers.base import DataMapper


class FakeORM(Base):
    __tablename__ = "fakes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]


class FakeSchema(BaseModel):
    id: int
    name: str


class FakeDataMapper(DataMapper):
    db_model = FakeORM
    schema = FakeSchema
