from src.drivers.requester_spy import RequesterSpy
from src.stages.transform import Tranformer
import pytest


@pytest.fixture
def data():
    data = {
        "adult": False,
        "backdrop_path": "/c1BaOxC8bo5ACFYkYYxL0bBWRaq.jpg",
        "belongs_to_collection": None,
        "budget": 4000000,
        "genres": [{"id": 80, "name": "Crime"}, {"id": 35, "name": "Comedy"}],
        "homepage": "https://www.miramax.com/movie/four-rooms/",
        "id": 5,
        "imdb_id": "tt0113101",
        "original_language": "en",
        "original_title": "Four Rooms",
        "overview": "It's Ted the Bellhop's first night on the job..."
        "and the hotel's "
        "very unusual guests are about to place him in some outrageous "
        "predicaments. It seems that this evening's room service is "
        "serving up one unbelievable happening after another.",
        "popularity": 18.872,
        "poster_path": "/75aHn1NOYXh4M7L5shoeQ6NGykP.jpg",
        "production_companies": [
            {
                "id": 14,
                "logo_path": "/m6AHu84oZQxvq7n1rsvMNJIAsMu.png",
                "name": "Miramax",
                "origin_country": "US",
            },
            {
                "id": 59,
                "logo_path": "/yH7OMeSxhfP0AVM6iT0rsF3F4ZC.png",
                "name": "A Band Apart",
                "origin_country": "US",
            },
        ],
        "production_countries": [
            {"iso_3166_1": "US", "name": "United States of America"}
        ],
        "release_date": "1995-12-09",
        "revenue": 4257354,
        "runtime": 98,
        "spoken_languages": [
            {"english_name": "English", "iso_639_1": "en", "name": "English"}
        ],
        "status": "Released",
        "tagline": "Twelve outrageous guests. Four scandalous requests."
        "And one lone "
        "bellhop, in his first day on the job, who's in for the wildest "
        "New year's Eve of his life.",
        "title": "Four Rooms",
        "video": False,
        "vote_average": 5.764,
        "vote_count": 2369,
    }
    return [data]


def test_transform(data):
    list_of_columns_chosed = [
        "title",
        "genres",
        "budget",
        "original_language",
        "original_title",
        "vote_average",
        "vote_count",
        "popularity",
        "revenue",
        "release_date",
        "status",
        "runtime",
    ]
    data = Tranformer().transform(data)
    for item in list_of_columns_chosed:
        assert item in data[0]
    assert len(data) == 1
