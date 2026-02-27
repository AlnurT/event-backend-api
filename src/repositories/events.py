from src.models import EventsOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.base import DataMapper
from src.repositories.mappers.mappers import EventDataMapper


class EventRepository(BaseRepository):
    model = EventsOrm
    mapper: DataMapper = EventDataMapper
