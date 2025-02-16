from app.words.technical.words_dto import WordsResponse, WordDetailResponse, WordBase
from app.words.technical.words_dto import WordsResponse, WordDetailResponse
from app.words.business.base_fetch_paginated_words import BaseFetchPaginatedWords
from app.words.business.base_fetch_word_details import BaseFetchWordDetails

class WordsController:
    def __init__(
        self,
        fetch_paginated_words: BaseFetchPaginatedWords,
        fetch_word_details: BaseFetchWordDetails
    ):
        self.fetch_paginated_words = fetch_paginated_words
        self.fetch_word_details = fetch_word_details

    async def get_words(
        self,
        page: int = 1,
        page_size: int = 100
    ) -> WordsResponse:
        return await self.fetch_paginated_words.execute(page, page_size)
    
    async def get_word_by_id(
        self,
        id: int
    ) -> WordDetailResponse:
        return await self.fetch_word_details.execute(id)
    