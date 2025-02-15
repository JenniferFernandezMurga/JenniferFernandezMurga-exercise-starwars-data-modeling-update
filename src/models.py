import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey, Integer
from eralchemy2 import render_er
from typing import List

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(8), nullable=False)
    favorites_caracteres: Mapped[List["Favorites_caracters"]] = relationship(back_populates="user")
    favorites_planetas: Mapped[List["Favorites_caracters"]] = relationship(back_populates="user")



class Favorites_caracters(Base):
    __tablename__ = 'favorites_caracters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    character_id: Mapped[int] = mapped_column(ForeignKey('characters.id'), nullable=False)

class Favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('user.id'), nullable=False)
    planets_id: Mapped[int] = mapped_column(ForeignKey('planets.id'), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=False)
    mass: Mapped[int] = mapped_column(Integer, nullable=False)
    birth_year: Mapped[int] = mapped_column(Integer, nullable=False)
    homeworld: Mapped[str] = mapped_column(String(50), nullable=False)
    favorites: Mapped[List["Favorites_caracters"]] = relationship("Favorites_caracters", back_populates="character")
    
    

class Planets(Base):
    __tablename__ = 'planets'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(String(50), nullable=False)
    population: Mapped[int] = mapped_column(Integer, nullable=False)
    diameter: Mapped[int] = mapped_column(Integer, nullable=False)
    orbital_period: Mapped[int] = mapped_column(Integer, nullable=False)
    favoritos: Mapped[List["Favorites_planets"]] = relationship("Favorites_planets", back_populates="planet")



    def to_dict(self):
        return {}




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
