from pprint import pprint

from example.app.models import MoodModel
from flaxx.pydantic_schema_generator import pydantic_model_creator

MoodSchema = pydantic_model_creator(MoodModel, name=f"{MoodModel.__name__}Schema")
MoodSchemaCreate = pydantic_model_creator(MoodModel, name=f"{MoodModel.__name__}SchemaCreate",
                                          exclude=("ts",),
                                          exclude_pk=True)

if __name__ == "__main__":
    print("\n\n\n\nSCHEMAS")
    pprint(MoodSchema.schema())
    pprint(MoodSchemaCreate.schema())
