"""Базовый репозиторий с общими CRUD-операциями.

Модуль предоставляет класс BaseRepository, который инкапсулирует
часто используемые операции с базой данных (через SQLAlchemy) и
сопоставление результатов в Pydantic-схемы через DataMapper.
"""

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
    """
    Универсальный репозиторий для работы с БД.

     Атрибуты класса (переопределяются в подклассах):
    - model: SQLAlchemy-модель (класс таблицы).
    - mapper (DataMapper): Маппер данных, который преобразует ORM-объекты
      в Pydantic-схемы.

     Экземпляр класса:
    - session: асинхронная сессия для выполнения SQL-запросов.

     Методы класса:
    - Методы возвращают Pydantic-схемы (SchemaType) или списки таких схем.
    - При конфликте уникальности выбрасывается ObjectAlreadyExistsException.
    - При отсутствии объекта выбрасывается ObjectNotFoundException.
    """

    model = None
    mapper: DataMapper = None

    def __init__(self, session):
        """
        Инициализация репозитория.

        :param session: асинхронная сессия для выполнения SQL-запросов.
        """
        self.session = session

    async def get_filtered(self, *filters, **filters_by) -> list[SchemaType | None]:
        """
        Получить объекты, соответствующие указанным фильтрам.

        :param filters: позиционные фильтры для выбора записи.
        :param filters_by: именованные фильтры для выбора записи.
        :return: список объектов, представленных в виде Pydantic-схем.
        """
        query = select(self.model).filter(*filters).filter_by(**filters_by)
        result = await self.session.execute(query)
        res_scalars = result.scalars().all()

        return [self.mapper.map_to_schema(model) for model in res_scalars]

    async def get_all(self) -> list[SchemaType | None]:
        """
        Получить все записи модели.

        :return: список всех записей, в виде Pydantic-схем.
        """
        return await self.get_filtered()

    async def add(self, data: Schema) -> SchemaType:
        """
        Добавить одну запись в базу.

        :param data: данные для вставки в виде Pydantic-схемы.
        :return: добавленная запись, в виде Pydantic-схемы.
        :raises ObjectAlreadyExistsException: если запись уже существует.
        :raises IntegrityError: если возникла другая ошибка целостности данных.
        """
        add_stmt = insert(self.model).values(**data.model_dump()).returning(self.model)

        try:
            result = await self.session.execute(add_stmt)
            res_scalar = result.scalars().one()
            return self.mapper.map_to_schema(res_scalar)

        except IntegrityError as ex:
            # Если причина - нарушение уникальности,
            # выбрасывает пользовательское исключение
            if isinstance(ex.orig, UniqueViolationError):
                raise ObjectAlreadyExistsException from ex

            # Иначе пробрасываем оригинальную ошибку
            raise ex

    async def add_many(self, data_list: list[Schema]) -> list[SchemaType]:
        """
        Добавить несколько записей за одну операцию.

        :param data_list: список данных для обновления в виде Pydantic-схем.
        :return: список добавленных записей, в виде Pydantic-схем.
        :raises ObjectAlreadyExistsException: если хотя бы одна запись уже существует.
        :raises IntegrityError: при других ошибках целостности.
        """
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
            # Если причина - нарушение уникальности,
            # выбрасывает пользовательское исключение
            if isinstance(ex.orig, UniqueViolationError):
                raise ObjectAlreadyExistsException from ex

            # Иначе пробрасываем оригинальную ошибку
            raise ex

    async def edit(
        self, data: Schema, exclude_unset: bool = False, **filters_by
    ) -> SchemaType:
        """
        Обновить существующую запись.

        :param data: данные для обновления в виде Pydantic-схемы.
        :param exclude_unset: если True, исключает неустановленные поля
          из преобразования.
        :param filters_by: именованные фильтры для выбора записи.
        :return: обновлённая запись, в виде Pydantic-схемы.
        :raises ObjectNotFoundException: если запись не найдена.
        """
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
        """
        Удалить запись, соответствующую фильтрам.

        :param filters_by: именованные фильтры для выбора записи.
        :return: удалённая запись, в виде Pydantic-схемы.
        :raises ObjectNotFoundException: если запись не найдена.
        """
        delete_stmt = delete(self.model).filter_by(**filters_by).returning(self.model)

        try:
            result = await self.session.execute(delete_stmt)
            res_scalar = result.scalars().one()
            return self.mapper.map_to_schema(res_scalar)

        except NoResultFound as ex:
            raise ObjectNotFoundException from ex
