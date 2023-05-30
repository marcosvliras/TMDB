from abc import ABC, abstractmethod


class RepoInterface(ABC):
    """Repository Interface."""

    @abstractmethod
    def select(self):
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def insert(
        self,
        idx: int,
        title: str,
        genres: str,
        budget: int,
        original_language: str,
        original_title: str,
        vote_average: float,
        vote_count: str,
        popularity: float,
        revenue: int,
        release_date: str,
        status: str,
        runtime: int,
    ):
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")

    @abstractmethod
    def delete(self, idx: int):
        """Must implement."""
        raise NotImplementedError("Abstract method not implemented.")
