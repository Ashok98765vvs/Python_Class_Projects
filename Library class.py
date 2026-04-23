class Library:
    branch_count = 0

    def __init__(self):
        self._books = {}
        Library.branch_count += 1

    @property
    def books(self):
        return self._books

    @books.setter
    def books(self, value):
        if not isinstance(value, dict):
            raise ValueError("Books must be stored in a dictionary format.")
        self._books = value

    def show_books(self):
        for title, (qty, author) in self._books.items():
            print(f"{title} - Author: {author}, Copies: {qty}")

    def add_book(self, title: str, author: str, copies: int):
        if title in self._books:
            qty, existing_author = self._books[title]
            self._books[title] = (qty + copies, existing_author)
        else:
            self._books[title] = (copies, author)

    def borrow(self, title: str):
        if title in self._books:
            qty, author = self._books[title]
            if qty > 0:
                self._books[title] = (qty - 1, author)
                print(f"{title} borrowed successfully.")
            else:
                print("Book not available.")
        else:
            print("Book not available.")

    @classmethod
    def get_branch_count(cls):
        return cls.branch_count


lib1 = Library()
lib2 = Library()
print("Library 1 created")
print("Library 2 created")
print("Total Branches:", Library.get_branch_count())

print("\nAdding books...")
lib1.add_book("Python Basics", "Guido van Rossum", 3)
print("Added: Python Basics")
lib1.add_book("Clean Code", "Robert Martin", 2)
print("Added: Clean Code")
lib1.add_book("Data Structures", "Thomas Cormen", 5)
print("Added: Data Structures")

print("\nAll Books in Library 1:")
lib1.show_books()

print("\nBorrowing Books...")
lib1.borrow("Python Basics")
lib1.borrow("Python Basics")
lib1.borrow("Python Basics")
lib1.borrow("Python Basics")

print("\nUpdated Books after borrowing:")
lib1.show_books()

print("\nAdding more copies of Python Basics...")
lib1.add_book("Python Basics", "Guido van Rossum", 2)

print("\nFinal Book List:")
lib1.show_books()

print("\nTesting invalid books setter...")
try:
    lib1.books = [1, 2, 3]
except ValueError as e:
    print("Error:", e)

print("\nTotal Library Branches:", Library.get_branch_count())