from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, name: str, year: int):
        self._name = name
        self.__year = year

    @property
    def year(self):
        return self.__year

    @abstractmethod
    def get_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, name, year):
        super().__init__(name, year)
        self.category = "Book"

    def get_info(self):
        return {
            "name": self._name,
            "year": self.year,
            "category": self.category
        }

class Magazine(LibraryItem):
    def __init__(self, name, year):
        super().__init__(name, year)
        self.category = "Magazine"

    def get_info(self):
        return {
            "name": self._name,
            "year": self.year,
            "category": self.category
        }
