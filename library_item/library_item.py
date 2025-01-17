"""
Description: A class to manage LibraryItem objects.
"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"
__credits__ = "Md Apurba Khan"

from genre.genre import Genre

class LibraryItem:
    """Represents a library item with title, author, and genre."""

    def __init__(self, title: str, author: str, genre: Genre):
        """
        Initializes a LibraryItem instance.

        Args:
            title (str): The title of the library item.
            author (str): The author of the library item.
            genre (Genre): The genre of the library item.

        Raises:
            ValueError: If title or author is blank or genre is invalid.
        """
        if not title.strip():
            raise ValueError("Title cannot be blank.")
        if not author.strip():
            raise ValueError("Author cannot be blank.")
        if not isinstance(genre, Genre):
            raise ValueError("Invalid Genre.")

        self.__title = title.strip()
        self.__author = author.strip()
        self.__genre = genre

    @property
    def title(self) -> str:
        """Returns the title of the library item."""
        return self.__title

    @property
    def author(self) -> str:
        """Returns the author of the library item."""
        return self.__author

    @property
    def genre(self) -> Genre:
        """Returns the genre of the library item."""
        return self.__genre