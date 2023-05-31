from src.infra.entities import Filmes
from sqlalchemy.orm.exc import NoResultFound
from .interface import RepoInterface


class FilmesRepo(RepoInterface):
    """Filme repository."""

    def __init__(self, connectionHandler) -> None:
        """Construct."""
        self.__connectionHandler = connectionHandler

    def select(self):
        """Select."""
        with self.__connectionHandler() as db:
            try:
                data = db.session.query(Filmes).all()
                return data
            except NoResultFound:
                raise None
            except Exception as e:
                db.session.rollback()
                raise e

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
        """Insert."""
        with self.__connectionHandler() as db:
            try:
                data_insert = Filmes(
                    idx=idx,
                    title=title,
                    genres=genres,
                    budget=budget,
                    original_language=original_language,
                    original_title=original_title,
                    vote_average=vote_average,
                    vote_count=vote_count,
                    popularity=popularity,
                    revenue=revenue,
                    release_date=release_date,
                    status=status,
                    runtime=runtime,
                )
                db.session.add(data_insert)
                db.session.commit()
                return data_insert
            except Exception as e:
                db.session.rollback()
                raise e

    def delete(self, idx: int):
        """Delete."""
        with self.__connectionHandler() as db:
            try:
                db.session.query(Filmes).filter(Filmes.idx == idx).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
