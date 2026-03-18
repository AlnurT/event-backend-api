"""
Модуль содержит класс DataMapper, который предоставляет методы для
сопоставления данных между Pydantic-схемами и моделями базы данных.
"""

from src.utils.utils import DBModelType, SchemaType


class DataMapper:
    """
    Класс для сопоставления данных между Pydantic-схемами и моделями базы данных.

     Атрибуты класса:
    - db_model: ORM-модель (SQLAlchemy).
    - schema: Pydantic-схема.
    """

    db_model: type[DBModelType] = None
    schema: type[SchemaType] = None

    @classmethod
    def map_to_db_model(
        cls, data: SchemaType, exclude_unset: bool = False
    ) -> DBModelType:
        """
        Преобразует данные из Pydantic-схемы в модель базы данных.

        :param data: Pydantic-схема.
        :param exclude_unset: если True, исключает неустановленные поля
          из преобразования.
        :return: ORM-модель базы данных.
        """
        return cls.db_model(**data.model_dump(exclude_unset=exclude_unset))

    @classmethod
    def map_to_schema(cls, data: DBModelType) -> SchemaType:
        """
        Преобразует данные из модели базы данных в Pydantic-схему.

        :param data: ORM-модель базы данных.
        :return: Pydantic-схема.
        """
        return cls.schema.model_validate(data, from_attributes=True)
