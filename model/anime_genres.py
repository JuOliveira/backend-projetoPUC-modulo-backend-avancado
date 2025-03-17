from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from  model import Base

class AnimeGenres(Base):
   __tablename__ = 'anime_genres'

   anime_id = Column(Integer, ForeignKey('anime_list.id'))
   genres_id = Column(Integer, ForeignKey('genres.id'))