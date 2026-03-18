"""Репозиторий для работы с участниками.

Модуль предоставляет класс UserRepository, который наследует атрибуты и методы
базового репозитория BaseRepository.
"""

from src.models import UsersOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.base import DataMapper
from src.repositories.mappers.mappers import UserDataMapper


class UserRepository(BaseRepository):
    """
    Репозиторий для работы с БД участников.

     Атрибуты:
    - model (UsersOrm): ORM-модель.
    - mapper (UserDataMapper): Маппер данных.
    """

    model = UsersOrm
    mapper: DataMapper = UserDataMapper
