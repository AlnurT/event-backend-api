"""
Утилитарные типы и перечисления для проекта.

Этот модуль содержит:
- параметры типизации DBModelType и SchemaType для использования в проекте.
"""

from enum import Enum
from typing import TypeVar

from pydantic import BaseModel
from src.database import Base


class UserLevel(str, Enum):
    beginner = "новичок"
    amateur = "любитель"
    medium = "средний"
    advanced = "продвинутый"
    pro = "профессионал"


# Параметры типизации:
# DBModelType ограничен базовым классом Base (SQLAlchemy DeclarativeBase),
# поэтому его можно использовать для обозначения типа ORM-моделей.
DBModelType = TypeVar("DBModelType", bound=Base)

# SchemaType ограничен pydantic.BaseModel и предназначен для Pydantic-схем.
SchemaType = TypeVar("SchemaType", bound=BaseModel)
