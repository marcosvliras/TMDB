from src.stages.extract import ExtractMovies
from src.drivers import Requester
from src.stages.transform import Tranformer
from src.infra.configs import Base, DBConnection
from src.infra.repository import FilmesRepo
from src.stages.load import LoadData


conn = DBConnection()
engine = conn.get_engine()
Base.metadata.create_all(bind=engine)


class MainPipeline:
    """Main Pipeline."""

    @staticmethod
    def execute():
        """Execute the main pipeline."""

        # não sabia se deveria enviar ou nao com minha chave de api
        # entao acabei enviando para nao ter nenhum problema
        # mas a ideia seria usar uma chave propria
        api_key = "a773e9c7af7861e875f8f9d6ada80d36"
        extractor = ExtractMovies(api_key, Requester)
        response = extractor.extract()
        response = Tranformer().transform(response)
        repository = FilmesRepo(DBConnection)
        loader = LoadData(repository)
        loader.load(response)
