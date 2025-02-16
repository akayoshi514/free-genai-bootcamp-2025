from typing import List
from pydantic import BaseModel
from app.schemas.pagination_dto import Pagination
#from .groups_dto import GroupItem

class WordStats(BaseModel):
    correct_count: int
    wrong_count: int

class WordBase(BaseModel):
    japanese: str
    romaji: str
    english: str

class WordItem(WordBase):
    correct_count: int
    wrong_count: int

class WordsResponse(BaseModel):
    items: List[WordItem]
    pagination: Pagination

class WordDetailResponse(WordBase):
    stats: WordStats
#    groups: List[GroupItem] 