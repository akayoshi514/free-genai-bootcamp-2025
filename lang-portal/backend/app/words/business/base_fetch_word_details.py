from abc import ABC, abstractmethod
from typing import Optional
from app.words.business.words_entities import Word

class BaseFetchWordDetails(ABC):
    """
    Abstract base class defining the interface for the fetch word details use case.
    This metaclass ensures that any implementing class provides the required methods
    for the fetch word details use case.
    """
        
    @abstractmethod
    async def execute(self, word_id: int) -> Optional[Word]:
        """
        Retrieve a specific word by its ID
        
        Args:
            word_id (int): The ID of the word to retrieve
            
        Returns:
            Optional[Word]: The Word entity if found, None otherwise
        """
        pass 