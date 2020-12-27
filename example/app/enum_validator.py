from tortoise.models import Model
import tortoise.fields
from enum import EnumMeta

from example.app.models import MoodModel
from schemas import MoodSchema
import enums


def validate(schema) -> (bool, str):
    for field in schema.Config.fields:
        for enum_name in dir(enums):
            enum = getattr(enums, enum_name)
            try:
                if enum is not None and issubclass(type(enum), EnumMeta):
                    if str(field).capitalize() == enum_name:
                        value = getattr(schema, field)
                        values = [v.value for v in enum]
                        if value in values:
                            return True, ""
                        else:
                            return False, f"'{value}' not in accepted values: {values}"
            except TypeError:
                print("Not an enum")


if __name__ == "__main__":
    validate(MoodSchema, MoodModel)
