from enum import Enum


class Mood(Enum):
    NEGATIVE = "negative"
    NEUTRAL = "neutral"
    POSITIVE = "positive"


if __name__ == "__main__":
    print(list(Mood))
