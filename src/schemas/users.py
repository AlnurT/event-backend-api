"""
Модуль содержит Pydantic-схему участников.

Содержит определение полей и их назначение в контексте схемы.
"""

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """
    Pydantic-схема участников.

     Атрибуты:
    - id (int): id участника.
    - email (str): почта (не более 50 символов, уникальная).
    - name (str): имя (не более 50 символов).
    - description (str | None): о себе.
    """

    id: int = Field(description="ID пользователя")
    email: EmailStr = Field(max_length=50, description="Почта")
    name: str = Field(max_length=50, description="Имя")
    description: str | None = Field(max_length=500, description="Описание")
