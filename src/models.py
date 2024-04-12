import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorite_characters = relationship('favoritepeople', back_populates='people')
    favorite_planets = relationship('favoritePlanet', back_populates='planet')

class Planets(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    planet_size = Column(String(250), nullable=False)
    planet_description = Column(String(250), nullable=False)
    planet_atmosphere = Column(String(250), nullable=False)
    favorite_planets = relationship('favoriteplanet', back_populates='planet')


class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    people_name = Column(String(250), nullable=False)
    people_age = Column(String(250), nullable=False)
    people_description = Column(String(250), nullable=False)
    people_affinity = Column(String(250), nullable=False)
    people_race = Column(String(250), nullable=False)
    people_favorite = relationship('favoritepeople', back_populates='people')

class FavoritePlanets(Base):
    __tablename__ = 'favorite_planets'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship('User', back_populates='favorite_planets')
    planet = relationship('Planet', back_populates='favorite_planets')

class FavoritepPople(Base):
    __tablename__ = 'favorite_peoples'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('people.id'))
    user = relationship('User', back_populates='favorite_peoples')
    character = relationship('People', back_populates='favorite_peoples')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
