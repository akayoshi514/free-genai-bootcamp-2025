from sqlalchemy import select
from app.words.technical.word_dbmodel import WordDbModel
from app.words.business.words_entities import Word, WordsPage
from app.words.business.base_words_fetcher import BaseWordFetcher

class WordRepository(BaseWordFetcher):
    def __init__(self, db):
        self.db = db

    async def get_words(self, page: int = 1, pageSize: int = 100) -> WordsPage:
        skip = (page - 1) * pageSize
        words = self.db.query(WordDbModel).offset(skip).limit(pageSize)
        
        total = self.db.query(WordDbModel).count()

        return WordsPage(
            items=[self._to_word_entity(self._to_dbentity(w)) for w in words],
            current_page=page,
            total_pages=(total + pageSize - 1) // pageSize,
            total_items=total,
            items_per_page=pageSize 
        )
    
    async def get_word_by_id(self, id: int) -> Word:
        word = self.db.query(WordDbModel).filter(WordDbModel.id == id).first()

        return self._to_word_entity(self._to_dbentity(word))
    

    def _to_dbentity(self, model) -> Word:
        return Word(
            id=model.id,
            kanji=model.kanji,
            romaji=model.romaji,
            english=model.english,
            #parts=model.parts,
            #correct_count=sum(1 for r in model.review_items if r.correct),
            #wrong_count=len(model.review_items) - sum(1 for r in model.review_items if r.correct),
            #groups=model.groups,
            #review_items=model.review_items
        )

    def _to_word_entity(self, entity) -> Word:
        return Word(
            japanese=entity.kanji,
            romaji=entity.romaji,
            english=entity.english,
            #correct_count=entity.correct_count,
            #wrong_count=entity.wrong_count
        )
    