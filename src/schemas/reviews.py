from datetime import date

from pydantic import BaseModel, Field


class ReviewSchema(BaseModel):
    """Базовая схема для отзывов мероприятий"""

    id: int = Field(description="ID отзыва")
    user_id: int = Field(description="ID участника")
    event_id: int = Field(description="ID мероприятия")
    review_data: date = Field(description="Дата отзыва")
    event_rating: int = Field(description="Оценка события")
    review_text: str | None = Field(max_length=500, description="Текст отзыва")
