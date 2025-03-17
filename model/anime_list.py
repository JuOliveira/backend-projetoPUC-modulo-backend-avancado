from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship

from  model import Base
from model.anime_genres import AnimeGenres

class AnimeList(Base):
    __tablename__ = 'anime_list'

    id = Column('pk_anime', Integer, primary_key=True)
    title_romaji = Column(String)
    title_native = Column(String)
    title_english = Column(String)
    description = Column(String)
    cover_image_medium = Column(String)
    cover_image_large = Column(String)
    start_date = Column(String)
    end_date = Column(String)
    status = Column(Integer)
    season = Column(String)
    episodes = Column(Integer)
    rating = Column(Integer)
    user_status = Column(Integer)
    is_favorite = Column(Boolean)
    genres = relationship('Genres', secondary=AnimeGenres, back_populates='anime_list')

    def __init__(self, id: int, title_romaji:str, title_native:str, title_english:str, description:str,
                cover_image_medium:str, cover_image_large:str, start_date:str, end_date:str, status:int,
                season:str, episodes:int, rating:int, user_status:int, is_favorite:bool):
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
