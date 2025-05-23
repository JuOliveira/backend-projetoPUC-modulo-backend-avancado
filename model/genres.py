from dataclasses import dataclass
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from  model import Base
from model.anime_genres import AnimeGenres
from model.manga_genres import MangaGenres

@dataclass
class Genres(Base):
    __tablename__ = 'genres'

    id:int = Column(Integer, primary_key=True)
    name:str = Column(String)
    anime_genres = relationship('AnimeList', secondary=AnimeGenres, back_populates='genres')
    manga_genres = relationship('MangaList', secondary=MangaGenres, back_populates='genres')

    def __init__(self, name:str):
      self.name = name