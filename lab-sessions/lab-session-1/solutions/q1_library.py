"""
Lab Session 1 — Question 1: Library Management System
Topics: Classes, Encapsulation, Properties, Special Methods (Week 1)
"""


class Book:
    def __init__(self, title: str, author: str, isbn: str, copies: int = 1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._copies = copies

    @property
    def copies(self) -> int:
        return self._copies

    @copies.setter
    def copies(self, value: int):
        if value < 0:
            raise ValueError("Number of copies cannot be negative")
        self._copies = value

    def __str__(self) -> str:
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', copies={self._copies})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

    def __hash__(self) -> int:
        return hash(self.isbn)


class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id
        self._borrowed_books: list = []

    @property
    def borrowed_books(self) -> list:
        return self._borrowed_books.copy()

    def borrow(self, book: Book):
        if book.copies <= 0:
            raise ValueError(f"No copies available for '{book.title}'")
        self._borrowed_books.append(book)
        book.copies -= 1

    def return_book(self, book: Book):
        if book not in self._borrowed_books:
            raise ValueError(f"'{book.title}' was not borrowed by {self.name}")
        self._borrowed_books.remove(book)
        book.copies += 1

    def __str__(self) -> str:
        return f"Member(name='{self.name}', id='{self.member_id}', borrowed={len(self._borrowed_books)})"


class Library:
    def __init__(self, name: str):
        self.name = name
        self._books: dict = {}
        self._members: dict = {}

    def add_book(self, book: Book):
        self._books[book.isbn] = book

    def register_member(self, member: Member):
        self._members[member.member_id] = member

    def find_book(self, isbn: str):
        return self._books.get(isbn)

    def get_member(self, member_id: str):
        return self._members.get(member_id)

    def __len__(self) -> int:
        return len(self._books)

    def __contains__(self, isbn: str) -> bool:
        return isbn in self._books


if __name__ == "__main__":
    print("=== Library Management System ===")

    # Create library
    lib = Library("YTU Central Library")

    # Create books
    b1 = Book("Clean Code", "Robert C. Martin", "978-0132350884", 3)
    b2 = Book("Design Patterns", "Gang of Four", "978-0201633610", 2)
    b3 = Book("Python Crash Course", "Eric Matthes", "978-1593279288", 5)

    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)

    # Create members
    alice = Member("Alice", "M001")
    bob = Member("Bob", "M002")
    lib.register_member(alice)
    lib.register_member(bob)

    print(f"Library: {lib.name}")
    print(f"Books: {len(lib)}")
    print(f"Members: 2")

    # Borrow/return
    print(f"\nAlice borrows 'Clean Code'...")
    alice.borrow(b1)
    print(f"Alice's borrowed books: {len(alice.borrowed_books)}")
    print(f"Clean Code copies remaining: {b1.copies}")

    print(f"\nBob borrows 'Clean Code'...")
    bob.borrow(b1)
    print(f"Clean Code copies remaining: {b1.copies}")

    print(f"\nAlice returns 'Clean Code'...")
    alice.return_book(b1)
    print(f"Clean Code copies remaining: {b1.copies}")

    # Equality and containment
    b1_duplicate = Book("Clean Code", "Robert C. Martin", "978-0132350884", 1)
    print(f"\nBook equality test: {b1 == b1_duplicate} (same ISBN)")
    print(f"Book in library: {'978-0132350884' in lib}")
    print(f"Library size: {len(lib)}")
