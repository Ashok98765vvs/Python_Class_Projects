class Library:
    branch_count = 0

    def __init__(self):
        Library.branch_count += 1
        self._books = {}

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, value):
        if not isinstance(value, dict):
            raise ValueError("Books must be stored in a dictionary format.")
        self._books = value

    def show_books(self):
        if not self._books:
            print("No books available in this library.")
            return
        for title, (copies, author) in self._books.items():
            print(f"Title: {title}, Author: {author}, Copies: {copies}")

    def add_book(self, title: str, author: str, copies: int):
        if title in self._books:
            existing_copies, existing_author = self._books[title]
            self._books[title] = (existing_copies + copies, existing_author)
        else:
            self._books[title] = (copies, author)

    def borrow(self, title: str):
        if title in self._books:
            copies, author = self._books[title]
            if copies > 0:
                self._books[title] = (copies - 1, author)
                print(f"You borrowed '{title}'. Remaining copies: {copies - 1}")
            else:
                print("Book not available.")
        else:
            print(f"'{title}' not found in library.")

    @classmethod
    def get_branch_count(cls):
        return cls.branch_count


lib1 = Library()
lib2 = Library()

print(f"Total Branches: {Library.get_branch_count()}")

lib1.add_book("Python Basics", "Guido van Rossum", 3)
lib1.add_book("Clean Code", "Robert Martin", 2)
lib1.add_book("Data Structures", "Thomas Cormen", 5)

lib1.show_books()

lib1.borrow("Python Basics")
lib1.borrow("Python Basics")
lib1.borrow("Python Basics")
lib1.borrow("Python Basics")

lib1.add_book("Python Basics", "Guido van Rossum", 2)

lib1.show_books()

try:
    lib1.books = ["not", "a", "dict"]
except ValueError as e:
    print(f"Error: {e}")