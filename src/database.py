from sqlalchemy import String
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from src.config import settings

engine = create_async_engine(settings.DB_URL, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

str_200 = String(200)
str_500 = String(500)


class Base(DeclarativeBase):
    pass
