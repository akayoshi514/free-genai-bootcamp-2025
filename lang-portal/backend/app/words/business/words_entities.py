from typing import List, Dict
from dataclasses import dataclass

@dataclass
class Word():
    id: int
    kanji: str
    romaji: str
    english: str
    parts: Dict[str, str]
    correct_count: int
    wrong_count: int
#    groups: List['Group']
#    review_items: List['WordReviewItem']

@dataclass
class WordStats():
    correct_count: int
    wrong_count: int

@dataclass
class WordsPage():
    items: List[Word]
    current_page: int
    total_pages: int
    total_items: int
    items_per_page: int 