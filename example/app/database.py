from tortoise import Tortoise

TORTOISE_ORM = {
    "connections": {"default": 'postgres://tim:pass@localhost:5432/recipe'},
    "apps": {
        "models": {
            "models": ["models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

async def get_db():
    await Tortoise.init(config=TORTOISE_ORM)

async def init():
    await Tortoise.init(config=TORTOISE_ORM)

    await Tortoise.generate_schemas()
