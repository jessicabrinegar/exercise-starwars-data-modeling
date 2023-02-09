import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    firstname = Column(String(200), nullable=False)
    lastname = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)

class Character(Base):
    __tablename__= 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    species = Column(String(250), nullable=True)
    birthyear = Column(String(250), nullable=True)
    homeworld = Column(Integer, ForeignKey('planet.id'), nullable=True)
    image = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__='planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=True)
    terrain = Column(String(250), nullable=True)
    diameter = Column(Integer, nullable=True)
    image = Column(String(250), nullable=False)

class Media(Base):
    __tablename__='media'
    id = Column(Integer, primary_key=True)
    media_type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)

class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class Comment(Base):
    __tablename__='comment'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)
    text = Column(String(250), nullable=False)

class Like(Base):
    __tablename__='like'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)  
    post_id = Column(Integer, ForeignKey('post.id'), nullable=True)    
    comment_id = Column(Integer, ForeignKey('post.id'), nullable=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
