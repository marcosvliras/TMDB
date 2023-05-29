from typing import Dict, List
import requests


class ExtractMovies:
    """Movies extraction class."""

    def __init__(self, api_key: str) -> None:
        """Construct.

        Parameters
        ----------
        api_key: str
            Api Key from TMDB.
        """
        self.__api_key = api_key

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
                response = requests.get(url, headers=headers)
                movies_list.append(response.json())
            except Exception as e:
                raise e(f"Esse id={movie_id} de filme pode estar com problema")

        return movies_list
