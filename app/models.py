class Book:
    """
    Класс для работы с книгами.

    Создержит атрибуты:
        id (int): Уникальный идентификатор.
        title (str): Название книги.
        author (str): Автор книги.
        year (int): Год издания.
        status (bool): Статус книги: "в наличии", "выдана").
    """
    _id_counter = 0
    status_book: dict = {True: "в наличии", False: "выдана"}

    def __init__(self, title, author, year, status=True):
        Book._id_counter += 1
        self.id = Book._id_counter
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return (
            f"id: {self.id},\n"
            f"title: {self.title},\n"
            f"author: {self.author},\n"
            f"year: {self.year},\n"
            f"status: {Book.status_book[self.status]}\n"
        )
