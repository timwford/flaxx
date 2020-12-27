import time

import uvicorn
from fastapi import FastAPI, HTTPException

from tortoise.contrib.fastapi import register_tortoise

from database import TORTOISE_ORM
from example.app.enum_validator import validate
from models import MoodModel
from enums import Mood
from schemas import MoodSchema, MoodSchemaCreate

app = FastAPI()

register_tortoise(app, config=TORTOISE_ORM)


@app.get("/")
async def root():
    return {"welcome": "http://127.0.0.1:5000/docs"}


@app.get("/mood", response_model=list[MoodSchema])
async def get_all_moods():
    all_moods = MoodModel.all()

    """
    moods = []
    async for r in all_moods.all():
        moods.append(r)
    """

    mood_schemas = await MoodSchema.from_queryset(all_moods)
    print("help")

    return mood_schemas


@app.post("/mood", status_code=201)
async def make_new_mood(new_mood: MoodSchemaCreate):
    valid, msg = validate(new_mood)

    if not valid:
        return HTTPException(status_code=422, detail=msg)

    new_mood_model = MoodModel(**new_mood.__dict__, ts=time.time())
    await new_mood_model.save()

    return new_mood


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=5000, log_level="info")
