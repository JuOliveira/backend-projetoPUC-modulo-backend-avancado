from typing import List
from pydantic import BaseModel

class MangaSchema(BaseModel):
    id: int 
    title_romaji: str 
    title_native: str 
    title_english: str
    description: str 
    cover_image_medium: str 
    cover_image_large: str
    start_date: str 
    end_date: str
    status: int 
    volumes: int 
    chapters: int 
    story: str
    art: str 
    rating: int
    user_status: int 
    is_favorite: bool 
    genres: List[str]

class MangaListSchema(BaseModel):
    data: List[MangaSchema]

class MangaSearchSchema(BaseModel):
    id: int