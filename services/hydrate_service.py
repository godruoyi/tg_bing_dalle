from .gushici import random_sentence
from .weather import get_weather2


class HydrateService:
    @staticmethod
    def random_sentence():
        return random_sentence()

    @staticmethod
    def get_weather(city: str):
        # disable fill weather info when city is not set
        if city is None or city == "":
            return ""
        return get_weather2(city)
