"""Репозиторий для работы с записями.

Модуль предоставляет класс RecordRepository, который наследует атрибуты и методы
базового репозитория BaseRepository.
"""

from src.models import RecordsOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.base import DataMapper
from src.repositories.mappers.mappers import RecordDataMapper


class RecordRepository(BaseRepository):
    """
    Репозиторий для работы с БД записей.

     Атрибуты:
    - model (RecordsOrm): ORM-модель.
    - mapper (RecordDataMapper): Маппер данных.
    """

    model = RecordsOrm
    mapper: DataMapper = RecordDataMapper
