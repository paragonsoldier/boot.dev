class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        books_to_keep = []
        for library_book in self.books:
            if library_book.title != book.title or library_book.author != book.author:
                books_to_keep.append(library_book)
        self.books = books_to_keep

    def search_books(self, search_string):
        found_books = []
        for book in self.books:
            if (
                search_string.lower() in book.title.lower() or
                search_string.lower() in book.author.lower()
            ):
                found_books.append(book)
        return found_books

            

