"""
Модуль содержит Pydantic-схему мероприятий.

Содержит определение полей и их назначение в контексте схемы.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class RecordSchema(BaseModel):
    """
    Pydantic-схема записей.

     Атрибуты:
    - id (int): id записи.
    - user_id (int): id участника.
    - event_id (int): id мероприятия.
    - datetime_from (datetime): дата и время начала мероприятия.
    - datetime_to (datetime): дата и время конца мероприятия.
    """

    id: int = Field(description="ID записи")
    user_id: int = Field(description="ID участника")
    event_id: int = Field(description="ID мероприятия")
    datetime_from: datetime = Field(description="Начало мероприятия")
    datetime_to: datetime = Field(description="Конец мероприятия")
