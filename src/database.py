"""
Модуль инициализации базы данных.

Задачи модуля:
- Создать асинхронные SQLAlchemy-движки и фабрики сессий для приложения.
- Предоставить вариант движка NullPool для тестов.
- Предоставить базовый класс Base для декларативных ORM-моделей.
"""

from sqlalchemy import NullPool, String
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from src.config import settings

# Асинхронный движок SQLAlchemy, использующий URL из настроек приложения.
engine = create_async_engine(settings.DB_URL, echo=True)

# Фабрика асинхронных сессий, привязанная к основному движку.
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)

# Асинхронный движок без пуллинга соединений для тестирования.
engine_null_pool = create_async_engine(settings.DB_URL, poolclass=NullPool)

# Фабрика асинхронных сессий для движка без пула.
async_session_null_pool = async_sessionmaker(
    bind=engine_null_pool, expire_on_commit=False
)

# SQLAlchemy-типовые объекты для колонок строк фиксированной длины.
str_20 = String(20)
str_50 = String(50)
str_500 = String(500)


class Base(DeclarativeBase):
    """
    Базовый класс для всех декларативных ORM-моделей в проекте.
    """

    pass
