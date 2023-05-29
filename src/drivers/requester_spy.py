from .interfaces import RequesterInterface
from typing import Dict
import json
import random


class RequesterSpy(RequesterInterface):
    """Requester."""

    def request(self, url: str = None, headers: Dict = None) -> Dict:
        """Request."""
        with open("src/drivers/data.json") as file:
            data = json.load(file)

        random_ = random.randint(0, 4)
        return data[random_]
