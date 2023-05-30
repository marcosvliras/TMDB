from src.stages.extract import ExtractMovies
from src.drivers import Requester, RequesterSpy
from src.stages.transform import Tranformer
import pprint
from src.infra.configs import Base, DBConnection

conn = DBConnection()
engine = conn.get_engine()
Base.metadata.create_all(bind=engine)


api_key = "a773e9c7af7861e875f8f9d6ada80d36"
ex = ExtractMovies(api_key, Requester)
r = ex.extract(qtd_movies=1)
r = Tranformer().transform(r)
pprint.pprint(r)
