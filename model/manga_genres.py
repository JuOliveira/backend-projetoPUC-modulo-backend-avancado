from sqlalchemy import Column, ForeignKey, Integer

from  model import Base

class MangaGenres(Base):
   __tablename__ = 'manga_genres'

   anime_id = Column(Integer, ForeignKey('manga_list.id'))
   genres_id = Column(Integer, ForeignKey('genres.id'))