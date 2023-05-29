from src.stages.extract import ExtractMovies
from src.drivers import RequesterSpy
from typing import List

api_key = "teste"


def test_extract():
    ex = ExtractMovies(api_key, RequesterSpy)
    data = ex.extract(qtd_movies=4)
    assert len(data) == 4
    assert isinstance(data, List)
    assert "title" in data[0]
