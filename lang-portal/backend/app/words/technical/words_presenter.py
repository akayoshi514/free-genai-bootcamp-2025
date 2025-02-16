from app.words.technical.words_dto import WordsResponse, WordBase
from app.words.business.words_entities import WordsPage, Word
from app.words.technical.words_dto import Pagination
from app.words.business.base_words_presenter import BaseWordsPresenter

class WordsPresenter(BaseWordsPresenter):
    async def present_words_page(
        self,
        words_page: WordsPage,
    ) -> WordsResponse:    
        return WordsResponse(
            items=[self._to_word_base(w) for w in words_page.items],
            pagination=self._to_pagination(words_page)
        )
    

    def _to_word_base(self, word) -> WordBase:
        return WordBase(
            japanese=word.kanji,
            romaji=word.romaji,
            english=word.english,
            #correct_count=word.correct_count,
            #wrong_count=word.wrong_count
        )
    
    
    def _to_pagination(self, words_page) -> Pagination:
        return Pagination(
            current_page=words_page.current_page,
            total_pages=words_page.total_pages,
            total_items=words_page.total_items,
            items_per_page=words_page.items_per_page 
        )

    async def present_word(
        self,
        word: Word
    ) -> WordBase:
        return self._to_word_base(word)