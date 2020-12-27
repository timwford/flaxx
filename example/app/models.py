from tortoise.models import Model
from tortoise import fields
from tortoise import run_async

from database import init
from enums import Mood


class MoodModel(Model):
    mood = fields.CharField(max_length=255,
                            null=False,
                            description=f"Mood being recorded: {[m.value for m in Mood]}")

    ts = fields.IntField(null=False,
                         description=f"Epoch time")

    def __str__(self):
        return f"Mood: {self.mood} Time: {self.ts}"


if __name__ == "__main__":
    run_async(init())
