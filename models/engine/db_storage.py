#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os


class DBStorage:
    """This class manages storage of hbnb models in a database"""
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine"""
        from sqlalchemy import create_engine
        from models.base_model import Base
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        hbnb_dev = os.getenv('HBNB_ENV')
        hbnb_dev_db = os.getenv('HBNB_MYSQL_DB')
        hbnb_dev_user = os.getenv('HBNB_MYSQL_USER')
        hbnb_dev_pwd = os.getenv('HBNB_MYSQL_PWD')
        hbnb_dev_host = os.getenv('HBNB_MYSQL_HOST')        

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(hbnb_dev_user, hbnb_dev_pwd,
                                              hbnb_dev_host, hbnb_dev_db),
                                      pool_pre_ping=True)
        
        # if 'hbnb_dev_db' not in self.__engine.table_names():
        #     Base.metadata.create_all(self.__engine)
        
        if hbnb_dev == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        if cls is not None:
            objs = self.__session.query(classes[cls]).all()
        else:
            objs = []
            for cls in classes.values():
                objs += self.__session.query(cls).all()
        return objs

    def new(self, obj):
        """Adds new object to storage"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes an object from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads objects from the database"""
        from sqlalchemy.orm import sessionmaker, scoped_session
        from models.base_model import Base

        # Reflect all tables in the database
        # Base.metadata.reflect(bind=self.__engine)

        # Drop all existing tables
        # Base.metadata.drop_all(bind=self.__engine)

        # Create all tables defined in your Base class
        Base.metadata.create_all(bind=self.__engine)

        # Create a new scoped session
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session())
        
    def close(self):
        """Closes the session"""
        self.__session.close()
