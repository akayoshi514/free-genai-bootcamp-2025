from fastapi import Depends

from app.config.database import get_db

from app.words.technical.word_repository import WordRepository
from app.words.technical.words_presenter import WordsPresenter
from app.words.technical.words_controller import WordsController
from app.words.business.fetch_paginated_words import FetchPaginatedWords
from app.words.business.fetch_word_details import FetchWordDetails

def get_words_controller(db=Depends(get_db)):
    repository = WordRepository(db)
    presenter = WordsPresenter()
    fetch_paginated_words = FetchPaginatedWords(repository, presenter)
    Fetch_word_details = FetchWordDetails(repository, presenter)
    return WordsController(fetch_paginated_words, Fetch_word_details)