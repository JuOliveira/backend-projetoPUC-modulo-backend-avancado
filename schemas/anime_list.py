from ctypes import Array
from typing import List
from pydantic import BaseModel

class AnimeSchema(BaseModel):
    id: int
    title_romaji: str
    title_native: str
    title_english: str
    description: str
    cover_image_medium: str
    cover_image_large: str
    start_date: str
    end_date: str
    status: str
    season: str
    episodes: int
    rating: int
    user_status: str
    is_favorite: bool
    genres: List[str]

class AnimeListSchema(BaseModel):
    data: List[AnimeSchema]

class AnimeSearchSchema(BaseModel):
    id: int