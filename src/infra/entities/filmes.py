from src.infra.configs import Base
from sqlalchemy import Column, String, Integer, Float


class Filmes(Base):
    """Filmes table."""

    __tablename__ = "filmes"

    idx = Column(Integer)
    title = Column(String)
    genres = Column(String)
    budget = Column(Integer)
    original_language = Column(String)
    original_title = Column(String)
    vote_average = Column(Float)
    vote_count = Column(Integer)
    popularity = Column(Float)
    revenue = Column(Integer)
    release_date = Column(String)
    status = Column(String)
    runtime = Column(Integer)

    def __repr__(self):
        """Repr method."""
        return f"""Filme(titulo={self.title}, genres={self.genres})"""
