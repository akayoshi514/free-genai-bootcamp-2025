from abc import ABC, abstractmethod
from app.words.business.words_entities import Word, WordsPage

class BaseWordFetcher(ABC):
    """
    Abstract base class defining the interface for word repositories.
    All word repository implementations should inherit from this class.
    """
    
    @abstractmethod
    async def get_words(self, page: int = 1, pageSize: int = 100) -> WordsPage:
        """
        Fetch a paginated list of words.
        
        Args:
            page (int): The page number to fetch (1-based indexing)
            pageSize (int): Number of items per page
            
        Returns:
            WordPage: Paginated word results
        """
        pass

    @abstractmethod
    async def get_word_by_id(self, id: int) -> Word:
        """
        Fetch detailed information for a specific word.
        
        Args:
            id (int): The ID of the word to fetch
            
        Returns:
            Word: The word entity with full details
        """
        pass
