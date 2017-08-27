#!/usr/bin/python

from sqlalchemy import Column, ForeignKey, Integer, String, Date, \
    Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class Country(Base):

    """
    Schema for country table
    """

    __tablename__ = 'country'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    user = relationship('User')
    cities = relationship('City', backref='Country')
    user_id = Column(Integer, ForeignKey('user.id'))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {'id': self.id, 'name': self.name,
                'cities': [i.serialize for i in self.cities]}


class City(Base):

    """
    Schema for city table
    """

    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    state = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    country = relationship('Country')
    user = relationship('User')
    country_id = Column(Integer, ForeignKey('country.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""

        return {
            'id': self.id,
            'name': self.name,
            'state': self.state,
            'description': self.description,
            'country_id': self.country_id,
            }


engine = create_engine('sqlite:///data.db')
Base.metadata.create_all(engine)
