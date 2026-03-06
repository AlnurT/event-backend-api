from asyncpg import UniqueViolationError
from pydantic import BaseModel as Schema
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError
from src.exceptions import ObjectAlreadyExistsException
from src.repositories.mappers.base import DataMapper
from src.utils.utils import SchemaType


class BaseRepository:
    """Базовый репозиторий для работы с БД"""

    model = None
    mapper: DataMapper = None

    def __init__(self, session):
        self.session = session

    async def get_filtered(self, *filters, **filters_by) -> list[SchemaType | None]:
        """Получить отфильтрованный список данных"""

        query = select(self.model).filter(*filters).filter_by(**filters_by)
        result = await self.session.execute(query)
        res_scalars = result.scalars().all()

        return [self.mapper.map_to_schema(model) for model in res_scalars]

    async def get_all(self) -> list[SchemaType | None]:
        """Получить весь список данных"""

        return await self.get_filtered()

    async def add(self, data: Schema) -> SchemaType:
        """Добавить данные"""

        add_stmt = insert(self.model).values(**data.model_dump()).returning(self.model)

        try:
            result = await self.session.execute(add_stmt)
            res_scalar = result.scalars().one()
            return self.mapper.map_to_schema(res_scalar)

        except IntegrityError as ex:
            if isinstance(ex.orig, UniqueViolationError):
                raise ObjectAlreadyExistsException from ex

            raise ex

    async def edit(
        self, data: Schema, exclude_unset: bool = False, **filters_by
    ) -> None:
        """Изменить данные по фильтру"""

        data_model = self.mapper.map_to_db_model(data, exclude_unset)
        edit_stmt = update(self.model).filter_by(**filters_by).values(data_model)
        await self.session.execute(edit_stmt)

    async def delete(self, **filters_by) -> None:
        """Удалить данные по фильтру"""

        delete_stmt = delete(self.model).filter_by(**filters_by)
        await self.session.execute(delete_stmt)
