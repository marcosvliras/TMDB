from src.infra.repository.interface import RepoInterface
from typing import Dict


class LoadData:
    """Load class."""

    def __init__(self, repository: RepoInterface) -> None:
        """Construct."""
        self.__repo = repository

    def load(self, transformed_data: Dict):
        """Load on database."""
        try:
            for key, value in transformed_data.items():
                self.__repo.insert(
                    idx=key,
                    title=value["title"],
                    genres=value["genres"],
                    budget=value["budget"],
                    original_language=value["original_language"],
                    original_title=value["original_title"],
                    vote_average=value["vote_average"],
                    vote_count=value["vote_count"],
                    popularity=value["popularity"],
                    revenue=value["revenue"],
                    release_date=value["release_date"],
                    status=value["status"],
                    runtime=value["runtime"],
                )
        except Exception as e:
            raise e

        print("Dados carregados com sucesso!")
