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


DBModelType = TypeVar("DBModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)
