#!/usr/bin/python3
"""This module defines the DBStorage class for MySQL-based persistence."""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """DBStorage class that manages MySQL storage via SQLAlchemy."""

    __engine = None
    __session = None

    def __init__(self):
        """Creates the SQLAlchemy engine linked to the MySQL database."""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST', 'localhost')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(user, pwd, host, db),
            pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Queries all objects of a given class, or all classes if cls=None."""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = [User, State, City, Amenity, Place, Review]
        result = {}
        query_classes = [cls] if cls else classes
        for klass in query_classes:
            if isinstance(klass, str):
                klass = {c.__name__: c for c in classes}.get(klass)
                if klass is None:
                    continue
            for obj in self.__session.query(klass).all():
                key = "{}.{}".format(type(obj).__name__, obj.id)
                result[key] = obj
        return result

    def new(self, obj):
        """Adds obj to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables and initializes the database session."""
        from models.base_model import Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)

    def close(self):
        """Closes the current session."""
        self.__session.remove()
