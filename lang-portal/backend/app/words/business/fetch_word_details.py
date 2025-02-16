from typing import Optional

from app.words.business.words_entities import Word
from app.words.business.base_words_fetcher import BaseWordFetcher
from app.words.business.base_fetch_word_details import BaseFetchWordDetails
from app.words.business.base_words_presenter import BaseWordsPresenter

class FetchWordDetails(BaseFetchWordDetails):
    def __init__(self, repository: BaseWordFetcher, presenter: BaseWordsPresenter):
        self.repository = repository
        self.presenter = presenter 

    async def execute(self, word_id: int) -> Optional[Word]:
        word = await self.repository.get_word_by_id(word_id) 
        return await self.presenter.present_word(word)
     