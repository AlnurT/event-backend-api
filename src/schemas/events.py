from pydantic import BaseModel, Field
from src.utils.enum_utils import UserLevel


class EventSchema(BaseModel):
    """Базовая схема для мероприятий"""

    id: int = Field(description="ID мероприятия")
    organizer_id: int = Field(description="ID организатора")
    event_name: str = Field(max_length=50, description="Название мероприятия")
    min_event_level: UserLevel = Field(
        default=UserLevel.amateur, description="Минимальный уровень события"
    )
    description: str | None = Field(max_length=500, description="Описание")
