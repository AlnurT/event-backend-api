from datetime import datetime

from pydantic import BaseModel, Field


class RecordSchema(BaseModel):
    """Базовая схема для записей мероприятий"""

    id: int = Field(description="ID записи")
    user_id: int = Field(description="ID участника")
    event_id: int = Field(description="ID мероприятия")
    datetime_from: datetime = Field(description="Начало события")
    datetime_to: datetime = Field(description="Конец события")
