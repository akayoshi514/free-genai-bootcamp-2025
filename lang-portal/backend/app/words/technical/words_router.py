from fastapi import APIRouter, HTTPException, Depends

from app.words.technical.words_dto import WordsResponse, WordDetailResponse
from app.words.technical.words_controller import WordsController
from app.words.technical.words_dependencies import get_words_controller

words_router = APIRouter(prefix="/api/words", tags=["Words"])

@words_router.get("", response_model=WordsResponse)
async def get_words(
    page: int = 1,
    page_size: int = 100,
    words_controller: WordsController = Depends(get_words_controller)
) -> WordsResponse:
    return await words_controller.get_words(page, page_size)

@words_router.get("/{id}", response_model=WordDetailResponse)
async def get_word_by_id(
    id: int,
    words_controller: WordsController = Depends(get_words_controller)
) -> WordDetailResponse:
    word = await words_controller.get_word_by_id(id)
    if word is None:
        raise HTTPException(status_code=404, detail="Word not found")
    return word
    