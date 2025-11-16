from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def add(self):
        pass 

class Book(LibraryItem):
    def add(self):
        return "Bark"

class Magazine(LibraryItem):
    def add(self):
        return "woof"
