from abc import ABC, abstractmethod
from app.words.technical.words_dto import WordsResponse, WordBase
from app.words.business.words_entities import WordsPage, Word

class BaseWordsPresenter(ABC):
    """
    Abstract interface for words presenter implementations.
    Defines the contract for presenting word-related data.
    """
    
    @abstractmethod
    async def present_words_page(
        self,
        words_page: WordsPage,
    ) -> WordsResponse:
        """
        Present a page of words.
        
        Args:
            words_page: WordsPage object containing paginated word data
            
        Returns:
            WordsResponse containing formatted word data for the API
        """
        pass

    @abstractmethod
    async def present_word(
        self,
        word: Word
    ) -> WordBase:
        """
        Present a single word.
        
        Args:
            word: Word entity to be presented
            
        Returns:
            WordBase containing formatted word data for the API
        """
        pass 