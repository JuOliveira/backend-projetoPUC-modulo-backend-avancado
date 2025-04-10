from dataclasses import dataclass
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship, Mapped
from typing import List

from  model import Base
from model.anime_genres import AnimeGenres
from model.genres import Genres

@dataclass
class AnimeList(Base):
    __tablename__ = 'anime_list'

    id:int = Column(Integer, primary_key=True)
    title_romaji:str = Column(String)
    title_native:str = Column(String)
    title_english:str = Column(String)
    description:str = Column(String)
    cover_image_medium:str = Column(String)
    cover_image_large:str = Column(String)
    start_date:str = Column(String)
    end_date:str = Column(String)
    status:str = Column(String)
    season:str = Column(String)
    episodes:int = Column(Integer)
    rating:int = Column(Integer)
    user_status:str = Column(String)
    is_favorite:bool = Column(Boolean)
    genres: Mapped[List[Genres]] = relationship('Genres', secondary=AnimeGenres, back_populates='anime_genres')

    def __init__(self, id: int, title_romaji:str, title_native:str, title_english:str, description:str,
                cover_image_medium:str, cover_image_large:str, start_date:str, end_date:str, status:str,
                season:str, episodes:int, rating:int, user_status:str, is_favorite:bool):
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
        self.season = season
        self.episodes = episodes
        self.rating = rating
        self.user_status = user_status
        self.is_favorite = is_favorite
