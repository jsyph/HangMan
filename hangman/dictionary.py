import json
import random
from typing import Dict
import hangman.utils as utils


class Dictionary:
    def __init__(self) -> None:
        with open(utils.get_asset_path("dictionary.json"), "r") as file:
            self.data: Dict = json.loads(file.read())

    def random_word(self) -> str:
        random_entry = random.choice(list(self.data.items()))

        return random_entry[0]
