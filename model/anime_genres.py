from dataclasses import dataclass
from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from  model import Base

AnimeGenres = Table('anime_genres', Base.metadata, 
   Column('anime_id', Integer, ForeignKey('anime_list.id'), primary_key=True),
   Column('genres_id', Integer, ForeignKey('genres.id'), primary_key=True)   
)