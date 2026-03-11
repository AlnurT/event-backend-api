from asyncpg import UniqueViolationError
from pydantic import BaseModel as Schema
from sqlalchemy import delete, insert, select, update
from sqlalchemy.exc import IntegrityError, NoResultFound
from src.exceptions import (
    ObjectAlreadyExistsException,
    ObjectNotFoundException,
)
from src.repositories.mappers.base import DataMapper
from src.utils.utils import SchemaType


class BaseRepository:
    model = None
    mapper: DataMapper = None

    def __init__(self, session):
        self.session = session

    async def get_filtered(self, *filters, **filters_by) -> list[SchemaType | None]:
        query = select(self.model).filter(*filters).filter_by(**filters_by)
        result = await self.session.execute(query)
        res_scalars = result.scalars().all()

        return [self.mapper.map_to_schema(model) for model in res_scalars]

    async def get_all(self) -> list[SchemaType | None]:
        return await self.get_filtered()

    async def add(self, data: Schema) -> SchemaType:
        add_stmt = insert(self.model).values(**data.model_dump()).returning(self.model)

        try:
            result = await self.session.execute(add_stmt)
            res_scalar = result.scalars().one()
            return self.mapper.map_to_schema(res_scalar)

        except IntegrityError as ex:
            if isinstance(ex.orig, UniqueViolationError):
                raise ObjectAlreadyExistsException from ex

            raise ex

    async def add_many(self, data_list: list[Schema]) -> list[SchemaType]:
        add_stmt = (
            insert(self.model)
            .values([data.model_dump() for data in data_list])
            .returning(self.model)
        )

        try:
            result = await self.session.execute(add_stmt)
            res_scalars = result.scalars().all()
            return [self.mapper.map_to_schema(model) for model in res_scalars]

        except IntegrityError as ex:
            if isinstance(ex.orig, UniqueViolationError):
                raise ObjectAlreadyExistsException from ex

            raise ex

    async def edit(
        self, data: Schema, exclude_unset: bool = False, **filters_by
    ) -> SchemaType:
        edit_stmt = (
            update(self.model)
            .filter_by(**filters_by)
            .values(**data.model_dump(exclude_unset=exclude_unset))
            .returning(self.model)
        )

        try:
            result = await self.session.execute(edit_stmt)
            res_scalar = result.scalars().one()
            return self.mapper.map_to_schema(res_scalar)

        except IntegrityError as ex:
            raise ObjectNotFoundException from ex

    async def delete(self, **filters_by) -> SchemaType:
        delete_stmt = delete(self.model).filter_by(**filters_by).returning(self.model)

        try:
            result = await self.session.execute(delete_stmt)
            res_scalar = result.scalars().one()
            return self.mapper.map_to_schema(res_scalar)

        except NoResultFound as ex:
            raise ObjectNotFoundException from ex
