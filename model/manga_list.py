from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from  model import Base
from model.manga_genres import MangaGenres

class MangaList(Base):
    __tablename__ = 'manga_list'

    id = Column('pk_manga', Integer, primary_key=True)
    title_romaji = Column(String)
    title_native = Column(String)
    title_english = Column(String)
    description = Column(String)
    cover_image_medium = Column(String)
    cover_image_large = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    status = Column(Integer)
    volumes = Column(Integer)
    chapters = Column(Integer)
    story = Column(String)
    art = Column(String)
    rating = Column(Integer)
    user_status = Column(Integer)
    is_favorite = Column(Boolean)
    genres = relationship('Genres', secondary=MangaGenres, back_populates='manga_list')

    def __init__(self, id:int, title_romaji:str, title_native:str, title_english:str, description:str,
                cover_image_medium:str, cover_image_large:str, start_date:str, end_date:str, status:int,
                volumes:int, chapters:int, story:str, art:str, rating:int, user_status:int, is_favorite:bool):
        self.id = id
        self.title_romaji = title_romaji
        self.title_native = title_native
        self.title_english = title_english
        self.description = description
        self.cover_image_medium = cover_image_medium
        self.cover_image_large = cover_image_large
        self.start_date = start_date
        self.end_date = end_date
        self.status = status
        self.volumes = volumes
        self.chapters = chapters
        self.story = story
        self.art = art
        self.rating = rating
        self.user_status = user_status
        self.is_favorite = is_favorite