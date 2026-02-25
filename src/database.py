from sqlalchemy import NullPool, String
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from src.config import settings

engine = create_async_engine(settings.DB_URL, echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

engine_null_pool = create_async_engine(settings.DB_URL, poolclass=NullPool)
async_session_null_pool = async_sessionmaker(
    bind=engine_null_pool, expire_on_commit=False
)

str_50 = String(50)
str_200 = String(200)
str_500 = String(500)


class Base(DeclarativeBase):
    pass
