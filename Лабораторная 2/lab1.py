class Book:
    def __init__(self, id_, name, pages):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        return f"Книга '{self.name}'"

    def __repr__(self):
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    def __init__(self, books=None):
        self.books = books if books is not None else []

    def get_next_book_id(self):
        if not self.books:
            return 1
        else:
            return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id):
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Can't find a book with this id.")

# Пример использования
if __name__ == "__main__":
    library = Library()
    book1 = Book(id_=library.get_next_book_id(), name='test_name_1', pages=200) #id == 1, ind == 0
    library.books.append(book1)

    book2 = Book(id_=library.get_next_book_id(), name='test_name_2', pages=200) #id == 2, ind == 1
    library.books.append(book2)

    print(library.books)  # Вывод списка книг
    print(library.get_index_by_book_id(1))  # Индекс книги с id=1
    print(library.get_index_by_book_id(2))
    print(library.get_index_by_book_id(3)) #id == 3, ind == None
