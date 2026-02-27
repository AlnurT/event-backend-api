from src.models import EventsOrm, RecordsOrm, ReviewsOrm, UsersOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.events import EventSchema
from src.schemas.records import RecordSchema
from src.schemas.reviews import ReviewSchema
from src.schemas.users import UserSchema


class UserDataMapper(DataMapper):
    db_model = UsersOrm
    schema = UserSchema


class EventDataMapper(DataMapper):
    db_model = EventsOrm
    schema = EventSchema


class RecordDataMapper(DataMapper):
    db_model = RecordsOrm
    schema = RecordSchema


class ReviewDataMapper(DataMapper):
    db_model = ReviewsOrm
    schema = ReviewSchema
