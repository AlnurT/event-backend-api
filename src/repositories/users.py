from src.models import UsersOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.base import DataMapper
from src.repositories.mappers.mappers import UserDataMapper


class UserRepository(BaseRepository):
    model = UsersOrm
    mapper: DataMapper = UserDataMapper
