import os
import json

from app.models import Book


class LibraryManager:
    """
    Менеджер библиотеки книг, позволяет производить загрузку из и сохранение в
    JSON файл. Используя его как БД.

    Атрибуты::
        library_file (str): Путь к JSON файлу.
        books (list): Список книг в библиотеке.
    """
    def __init__(self, library_file='books.json'):
        self.library_file = library_file
        self.books = self.load_books()

    def load_books(self):
        """Загрузка книг из JSON файла."""
        if os.path.exists(self.library_file):
            with open(self.library_file, 'r', encoding='utf-8') as file:
                return [
                    Book(
                        title=book['title'],
                        author=book['author'],
                        year=book['year'],
                        status=book['status']
                    ) for book in json.load(file)
                ]
        return []

    def save_books(self):
        """Сохранение книг в JSON файле."""
        with open(self.library_file, 'w', encoding='utf-8') as file:
            json.dump(
                [book.__dict__ for book in self.books],
                file,
                ensure_ascii=False,
                indent=4
            )

    def add_book(self, title, author, year):
        """Добавление книги в библиотеку."""
        new_book = Book(title=title, author=author, year=year)
        self.books.append(new_book)
        self.save_books()

        print(f'Книга добавлена:\nНазвание: {title},\nАвтор: {author}.\n')

    def delete_book(self, book_id):
        """Удаление книги из библиотеки по идентификатору."""
        book_to_delete = next(
            (book for book in self.books if book.id == book_id), None
        )
        if book_to_delete:
            self.books.remove(book_to_delete)
            self.save_books()
            print(f'Book with Id {book_id} deleted\n')
        else:
            print(f'Book with Id {book_id} not found\n')

    def find_books(self, **kwargs):
        """
        Поиск книг по параметрам.

        Args:
            **kwargs: Пары ключ-значение атрибутов для сопоставления.

        """
        all_books = self.books
        for key, value in kwargs.items():
            result = [
                book for book in all_books if getattr(book, key, None) == value
            ]
        return result

    def get_all_books(self):
        """Возвращает список книг в библиотеке."""
        return self.books

    def change_book_status(self, book_id, status):
        """Изменение статуса книги."""
        current_book = next(
            (book for book in self.books if book.id == book_id), None
        )
        if current_book:
            current_book.status = status
            self.save_books()
            if status is True:
                status_text = "в библиотеке"
            else:
                status_text = "выдана на руки"

            print(
                f"Для книгаи с id {book_id} изменен статус "
                f"на: '{status_text}.'\n")
        else:
            print("Книга не найдена\n")
