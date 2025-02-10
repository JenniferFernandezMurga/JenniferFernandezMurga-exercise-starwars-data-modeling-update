import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey, Integer
from eralchemy2 import render_er
from typing import List

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(nullable=False)

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(8), nullable=False)
    favoritos_caracteres: Mapped[List["Favorites_caracters"]] = relationship(back_populates="usuario")
    
# user = relationship('User', back_populates='favorites')


class Favorites_caracters(Base):
    __tablename__ = 'favoritos_caracters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'), nullable=False)
    character_id: Mapped[int] = mapped_column(ForeignKey('characters.id'), nullable=False)
    #Como se pondría una clave foranea y un nullable=false? y un max de (String(50) con un nullable?)

class Favorites_planets(Base):
    __tablename__ = 'favorites_planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey('usuario.id'), nullable=False)
    planets_id: Mapped[int] = mapped_column(ForeignKey('planets.id'), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    height: Mapped[int] = mapped_column(Integer, nullable=True)
    mass: Mapped[int] = mapped_column(Integer, nullable=True)
    birth_year: Mapped[int] = mapped_column(Integer, nullable=True)
    homeworld: Mapped[str] = mapped_column(String(50), nullable=True)
    favoritos: Mapped[List["Favorites_caracters"]] = relationship("Favorites_caracters", back_populates="character")
    
    

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    climate: Mapped[str] = mapped_column(String(50), nullable=True)
    population: Mapped[int] = mapped_column(Integer, nullable=True)
    diameter: Mapped[int] = mapped_column(Integer, nullable=True)
    orbital_period: Mapped[int] = mapped_column(Integer, nullable=True)
    favoritos: Mapped[List["Favorites_planets"]] = relationship("Favorites_planets", back_populates="planet")

    







# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id: Mapped[int] = mapped_column(primary_key=True)
#     street_name: Mapped[str]
#     street_number: Mapped[str]
#     post_code: Mapped[str] = mapped_column(nullable=False)





    def to_dict(self):
        return {}




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
