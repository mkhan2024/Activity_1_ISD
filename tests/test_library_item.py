"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
__author__ = "ACE Faculty"
__version__ = "1.1.0"

import unittest
from library_item.library_item import LibraryItem
from genre.genre import Genre

class TestLibraryItem(unittest.TestCase):
    def test_valid_initialization(self):
        item = LibraryItem("Test Title", "Test Author", Genre.FICTION)
        self.assertEqual(item.title, "Test Title")
        self.assertEqual(item.author, "Test Author")
        self.assertEqual(item.genre, Genre.FICTION)

    def test_blank_title(self):
        with self.assertRaises(ValueError):
            LibraryItem("", "Test Author", Genre.FICTION)

    def test_blank_author(self):
        with self.assertRaises(ValueError):
            LibraryItem("Test Title", "", Genre.FICTION)

    def test_invalid_genre(self):
        with self.assertRaises(ValueError):
            LibraryItem("Test Title", "Test Author", "Invalid Genre")