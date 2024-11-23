import json
import random
from typing import Dict
import os

DICTIONARY_FILE = os.path.dirname(__file__) + "/dictionary.json"


class Dictionary:
    def __init__(self) -> None:
        with open(DICTIONARY_FILE, "r") as file:
            self.data: Dict = json.loads(file.read())

    def random_word(self) -> str:
        random_entry = random.choice(list(self.data.items()))

        return random_entry[0]
