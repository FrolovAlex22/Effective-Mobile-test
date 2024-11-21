import unittest
import os

from app.utils import LibraryManager


class TestLibrary(unittest.TestCase):

    def setUp(self):
        """Создание тестовой библиотеки. Добавление тестовых книг."""
        self.library = LibraryManager(library_file="test_library.json")
        self.library.add_book("first book", "first author", 2001)
        self.library.add_book("second book", "second author", 2002)
        self.library.add_book("third book", "third author", 2003)

    def tearDown(self):
        """Удаление тестовой библиотеки. """
        if os.path.exists("test_library.json"):
            os.remove("test_library.json")

    def test_add_book(self):
        """Добавление книги в библиотеку."""
        self.library.add_book("Книга 1", "Атор 1", 2000)
        book = self.library.find_books(title="Книга 1")[0]
        self.assertEqual(book.title, "Книга 1")
        self.assertEqual(book.author, "Атор 1")
        self.assertEqual(book.year, 2000)
        self.assertEqual(book.status, True)

    def test_delete_book(self):
        """Удаление книги из библиотеки."""
        book = self.library.find_books(title="first book")[0]
        self.library.delete_book(book.id)
        books = self.library.find_books(title="first book")
        self.assertEqual(len(books), 0)

    def test_find_books(self):
        """Поиск книг по параметрам."""
        books = self.library.find_books(author="second author")
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "second book")

    def test_get_all_books(self):
        """Получение всех книг в библиотеке."""
        books = self.library.get_all_books()
        self.assertEqual(len(books), 3)

    def test_change_status(self):
        """Изменение статуса книги."""
        book = self.library.find_books(title="third book")[0]
        self.library.change_book_status(book.id, False)
        book = self.library.find_books(title="third book")[0]
        self.assertEqual(book.status, False)


if __name__ == "__main__":
    unittest.main()
