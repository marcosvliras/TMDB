from typing import Dict, List, Union
import pprint


class Tranformer:
    """TransformClass."""

    def __init__(self) -> None:
        """Construct."""
        pass

    def transform(self, data: List[Dict]) -> Dict:
        """Tranform data.

        Parameters
        ----------
        data: List[Dict]
            Data to be transformed
        """
        select_data = {}
        final_data = {}
        for idx, element in enumerate(data):
            select_data["title"] = element["title"]
            select_data["genres"] = self.__transform_genres(element["genres"])
            select_data["budget"] = element["budget"]
            select_data["original_language"] = element["original_language"]
            select_data["original_title"] = element["original_title"]
            select_data["vote_average"] = element["vote_average"]
            select_data["vote_count"] = element["vote_count"]
            select_data["popularity"] = element["popularity"]
            select_data["revenue"] = element["revenue"]
            select_data["release_date"] = element["release_date"]
            select_data["status"] = element["status"]
            select_data["runtime"] = element["runtime"]
            data = select_data.copy()
            final_data.update({idx: data})
        return final_data

    @staticmethod
    def __transform_genres(data: Union[List[Dict], Dict]) -> List:
        """Get the genres name.

        Parameters
        ----------
        data: List[Dict]
            Example
            data = [{'id': 80, 'name': 'Crime'}, {'id': 35, 'name': 'Comedy'}]
        """
        if isinstance(data, list):
            genres = []
            for genre in data:
                genres.append(genre["name"])
            return f"{genres}"
        elif isinstance(data, Dict):
            return [data["name"]]
        else:
            raise NameError()
