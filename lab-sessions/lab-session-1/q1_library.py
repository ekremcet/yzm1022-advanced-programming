"""
Lab Session 1 — Question 1: Library Management System
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME: 
STUDENT ID: 
"""


# YOUR CODE HERE


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Library Management System ===")

    lib = Library("YTU Central Library")

    b1 = Book("Clean Code", "Robert C. Martin", "978-0132350884", 3)
    b2 = Book("Design Patterns", "Gang of Four", "978-0201633610", 2)
    b3 = Book("Python Crash Course", "Eric Matthes", "978-1593279288", 5)

    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)

    alice = Member("Alice", "M001")
    bob = Member("Bob", "M002")
    lib.register_member(alice)
    lib.register_member(bob)

    print(f"Library: {lib.name}")
    print(f"Books: {len(lib)}")
    print(f"Members: 2")

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

    b1_duplicate = Book("Clean Code", "Robert C. Martin", "978-0132350884", 1)
    print(f"\nBook equality test: {b1 == b1_duplicate} (same ISBN)")
    print(f"Book in library: {'978-0132350884' in lib}")
    print(f"Library size: {len(lib)}")
