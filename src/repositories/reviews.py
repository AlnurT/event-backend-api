from src.models import ReviewsOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.base import DataMapper
from src.repositories.mappers.mappers import ReviewDataMapper


class ReviewRepository(BaseRepository):
    model = ReviewsOrm
    mapper: DataMapper = ReviewDataMapper
