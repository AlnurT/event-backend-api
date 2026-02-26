from pydantic import BaseModel, EmailStr, Field
from src.utils.enum_utils import UserLevel


class UserSchema(BaseModel):
    """Базовая схема для пользователя"""

    id: int = Field(description="ID пользователя")
    email: EmailStr = Field(max_length=50, description="Почта")
    name: str = Field(max_length=50, description="Имя")
    age: int = Field(ge=18, le=100, description="Возраст")
    phone_number: str = Field(max_length=20, description="Номер телефона")
    user_level: UserLevel = Field(
        default=UserLevel.amateur, description="Уровень участника"
    )
    description: str | None = Field(max_length=500, description="Описание")
