from sqlalchemy import Column, ForeignKey, Integer, Table

from  model import Base

MangaGenres = Table('manga_genres', Base.metadata , 
   Column('manga_id', Integer, ForeignKey('manga_list.id'), primary_key=True),
   Column('genres_id', Integer, ForeignKey('genres.id'), primary_key=True)   
)