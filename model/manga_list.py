from dataclasses import dataclass
from typing import List
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship, Mapped

from  model import Base
from model.genres import Genres
from model.manga_genres import MangaGenres

@dataclass
class MangaList(Base):
    __tablename__ = 'manga_list'

    id:int = Column(Integer, primary_key=True)
    title_romaji: str = Column(String)
    title_native:str = Column(String)
    title_english:str = Column(String)
    description:str = Column(String)
    cover_image_medium:str = Column(String)
    cover_image_large:str = Column(String)
    start_date:str = Column(String)
    end_date:str = Column(String)
    status:int = Column(Integer)
    volumes:int = Column(Integer)
    chapters:int = Column(Integer)
    story:str = Column(String)
    art:str = Column(String)
    rating:int = Column(Integer)
    user_status:int = Column(Integer)
    is_favorite:bool = Column(Boolean)
    genres:Mapped[List[Genres]] = relationship('Genres', secondary=MangaGenres, back_populates='manga_genres')

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