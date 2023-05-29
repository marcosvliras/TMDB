from .interfaces import RequesterInterface
from typing import Dict
import json
import requests


class Requester(RequesterInterface):
    """Requester."""

    def request(self, url: str, headers: Dict) -> Dict:
        """Request."""
        response = requests.get(url, headers=headers)
        return response.json()
