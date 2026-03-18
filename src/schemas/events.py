"""
Модуль содержит ORM-модель Pydantic-схему мероприятий.

Содержит определение полей и их назначение в контексте схемы.
"""

from pydantic import BaseModel, Field


class EventSchema(BaseModel):
    """
    Pydantic-схема мероприятий.

     Атрибуты:
    - id (int): id мероприятия.
    - organizer_id (int): id организатора.
    - event_name (str): название мероприятия (не более 50 символов).
    - description (str | None): описание мероприятия
      (необязательное поле, не более 500 символов).
    """

    id: int = Field(description="ID мероприятия")
    organizer_id: int = Field(description="ID организатора")
    event_name: str = Field(max_length=50, description="Название мероприятия")
    description: str | None = Field(max_length=500, description="Описание")
