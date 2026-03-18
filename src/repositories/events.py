"""Репозиторий для работы с мероприятиями.

Модуль предоставляет класс EventRepository, который наследует атрибуты и методы
базового репозитория BaseRepository.
"""

from src.models import EventsOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.base import DataMapper
from src.repositories.mappers.mappers import EventDataMapper


class EventRepository(BaseRepository):
    """
    Репозиторий для работы с БД событий.

     Атрибуты:
    - model (EventsOrm): ORM-модель.
    - mapper (EventDataMapper): Маппер данных.
    """

    model = EventsOrm
    mapper: DataMapper = EventDataMapper
