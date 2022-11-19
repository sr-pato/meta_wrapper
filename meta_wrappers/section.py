from abc import ABC, abstractmethod
from typing import List


class Section(ABC):
    """
    A section of an interactive message or menu.
    """

    @abstractmethod
    def __init__(self, title: str, rows: List[str]):
        """
        Creates a new section.
        """
        pass

    @abstractmethod
    def process(self):
        """
        Returns a section that the API understand.
        """
        pass
