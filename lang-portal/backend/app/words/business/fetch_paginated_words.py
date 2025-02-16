from typing import List

from app.words.business.words_entities import Word
from app.words.business.base_words_fetcher import BaseWordFetcher
from app.words.business.base_fetch_paginated_words import BaseFetchPaginatedWords
from app.words.business.base_words_presenter import BaseWordsPresenter

class FetchPaginatedWords(BaseFetchPaginatedWords):
    def __init__(self, repository: BaseWordFetcher, presenter: BaseWordsPresenter):
        self.repository = repository
        self.presenter = presenter

    async def execute(self, page: int, page_size: int) -> List[Word]:
        words_page = await self.repository.get_words(page, page_size)
        return await self.presenter.present_words_page(words_page)
        