from src.utils.utils import DBModelType, SchemaType


class DataMapper:
    db_model: type[DBModelType] = None
    schema: type[SchemaType] = None

    @classmethod
    def map_to_db_model(cls, data, exclude_unset: bool = False) -> DBModelType:
        return cls.db_model(**data.model_dump(exclude_unset=exclude_unset))

    @classmethod
    def map_to_schema(cls, data) -> SchemaType:
        return cls.schema.model_validate(data, from_attributes=True)
