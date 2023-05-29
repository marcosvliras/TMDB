from src.stages.extract import ExtractMovies
from src.drivers import Requester, RequesterSpy
import pprint

api_key = "a773e9c7af7861e875f8f9d6ada80d36"
ex = ExtractMovies(api_key, Requester)
r = ex.extract(qtd_movies=1)
pprint.pprint(r)
