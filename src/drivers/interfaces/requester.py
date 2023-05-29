from abc import ABC, abstractmethod
from typing import Dict


class RequesterInterface(ABC):
    """Requester Interface."""

    @abstractmethod
    def request(self) -> Dict[int, str]:
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")
