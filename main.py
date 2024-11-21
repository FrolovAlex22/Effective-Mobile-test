from app.utils import LibraryManager


def main():
    library = LibraryManager()
    print("Добро пожаловать в библиотеку!\n")

    while True:
        try:
            command = int(input("Выберите номер действия:\n"
                               "1: Добавление книги\n"
                               "2: Удаление книги\n"
                               "3: Поиск книги\n"
                               "4: Список книг в библиотеке\n"
                               "5: Изменить статус книги\n"
                               "6: Выход из приложения\n"
                               "Введите команду:"))
            if command == 1:
                title = input("Введите название книги:")
                author = input("Введите фамилию автора:")
                year = input("Укажите год выпуска:")
                if not year.isdigit():
                    print("Год выпуска должен быть числом\n")
                    while not year.isdigit():
                        year = input("Укажите год выпуска:")
                library.add_book(title=title, author=author, year=year)
                print("\n")

            elif command == 2:
                book_id = int(input("Введите id номер книги для удаления:"))
                library.delete_book(book_id=book_id)
                print("\n")

            elif command == 3:
                field = input(
                    "Пропишите текстом атрибут для поиска, нужно выбратьиз "
                    "списка(title/author/year): "
                )
                value = input(
                    f"Введите значение для поиска по атрибуту: {field}:"
                )
                if field == "id":
                    value = int(value)
                found_books = library.find_books(**{field: value})
                if found_books:
                    for book in found_books:
                        print("------------------")
                        print(book)
                else:
                    print("С подобным запросом ничего не найдено.\n")
                print("\n")

            elif command == 4:
                books = library.get_all_books()

                if books:
                    for book in books:
                        print(f"\n{book}")
                else:
                    print("Библиотека пуста.\n")

            elif command == 5:
                book_id = int(input(
                    "Введите id номер книги для изменения ее статуса:")
                )
                print("Изменение статуса книги:\n"
                      "1: в наличии\n"
                      "2: выдана\n")
                users_status = int(input("Выберите статус 1 или 2:"))
                while True:
                    if users_status == 1:
                        new_status = True
                        break
                    elif users_status == 2:
                        new_status = False
                        break
                    else:
                        print("Нужно ввести число 1 или 2\n")
                        users_status = int(input("Выберите статус:"))
                library.change_book_status(book_id=book_id, status=new_status)
                print("\n")

            elif command == 6:
                print("Работа библиотеки завершена\n")
                break

            else:
                print("Неправильная команда, нужно ввести число от 1 до 6\n")

        except Exception:
            print("Не корректный ввод.Нужно ввести число.\n")


if __name__ == "__main__":
    main()