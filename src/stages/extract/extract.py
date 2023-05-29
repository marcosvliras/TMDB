from src.drivers.interfaces import RequesterInterface
from typing import Dict, List
import requests


class ExtractMovies:
    """Movies extraction class."""

    def __init__(self, api_key: str, requester: RequesterInterface) -> None:
        """Construct.

        Parameters
        ----------
        api_key: str
            Api Key from TMDB.
        requester: RequesterInterface
            Api requester
        """
        self.__api_key = api_key
        self.__requester = requester()

    def extract(self, qtd_movies: int = 100) -> List[Dict]:
        """Extract.

        Parameters
        ----------
        qtd_movies: int, default = 100
            Amount of movies wanted to be got.
        """
        headers = {"accept": "application/json"}

        movies_list = []
        for movie_id in range(2, qtd_movies + 2):
            try:
                url = (
                    """https://api.themoviedb.org/3/"""
                    f"""movie/{movie_id}?api_key={self.__api_key}"""
                )
                response = self.__requester.request(url, headers)
                movies_list.append(response)
            except Exception as e:
                raise e

        return movies_list
