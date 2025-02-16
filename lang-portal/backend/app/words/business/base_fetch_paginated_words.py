from abc import ABC, abstractmethod
from typing import List
from app.words.business.words_entities import WordsPage

class BaseFetchPaginatedWords(ABC):
    """
    Abstract base class defining the interface for the fetch paginated words use case.
    This metaclass ensures that any implementing class provides the required methods
    for the fetch paginated words use case.
    """
        
    @abstractmethod
    async def execute(self, page: int, page_size: int) -> WordsPage:
        """
        Retrieve a paginated list of words
        
        Args:
            page (int): The page number to retrieve
            page_size (int): Number of items per page
            
        Returns:
            List[Word]: A list of Word entities
        """
        pass