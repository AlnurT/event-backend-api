"""Репозиторий для работы с отзывами.

Модуль предоставляет класс ReviewRepository, который наследует атрибуты и методы
базового репозитория BaseRepository.
"""

from src.models import ReviewsOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.base import DataMapper
from src.repositories.mappers.mappers import ReviewDataMapper


class ReviewRepository(BaseRepository):
    """
    Репозиторий для работы с БД отзывов.

     Атрибуты:
    - model (ReviewsOrm): ORM-модель.
    - mapper (ReviewDataMapper): Маппер данных.
    """

    model = ReviewsOrm
    mapper: DataMapper = ReviewDataMapper
