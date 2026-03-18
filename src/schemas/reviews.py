"""
Модуль содержит Pydantic-схему отзывов.

Содержит определение полей и их назначение в контексте схемы.
"""

from datetime import date

from pydantic import BaseModel, Field


class ReviewSchema(BaseModel):
    """
    Pydantic-схема отзывов.

     Атрибуты:
    - id (int): id отзыва.
    - user_id (int): id участника.
    - event_id (int): id мероприятия.
    - review_data (date): дата отзыва.
    - review_text (str | None): отзыв.
    """

    id: int = Field(description="ID отзыва")
    user_id: int = Field(description="ID участника")
    event_id: int = Field(description="ID мероприятия")
    review_data: date = Field(description="Дата отзыва")
    review_text: str | None = Field(max_length=500, description="Текст отзыва")
