from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBConnection:
    """DBConnection class."""

    def __init__(self) -> None:
        """Construct."""
        self.__connection = "sqlite:///./myDb.db"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        """Create database engine."""
        engine = create_engine(self.__connection)
        return engine

    def get_engine(self):
        """Return engine."""
        return self.__engine

    def __enter__(self):
        """Enter method."""
        session_make = sessionmaker(self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Exit method."""
        self.session.close()
