"""
Lab Session 5B - Question 3: Generic Data Structures - SOLUTION
YZM1022 Advanced Programming
"""

from typing import TypeVar, Generic, Iterator, List

T = TypeVar("T")


class Stack(Generic[T]):
    """Generic stack that works with any type T."""

    def __init__(self):
        self._items: List[T] = []

    def push(self, item: T) -> None:
        """Add item to the top of the stack."""
        self._items.append(item)

    def pop(self) -> T:
        """Remove and return the top item (raise IndexError if empty)."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> T:
        """Return the top item without removing it (raise IndexError if empty)."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """True if the stack has no items."""
        return len(self._items) == 0

    def __len__(self) -> int:
        """Number of items."""
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        """Iterate from top to bottom."""
        return reversed(self._items)


class Point:
    """Custom Point class for demonstrating the stack with a custom type."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"


def is_balanced(expression: str) -> bool:
    """Use your Stack to check whether the brackets in `expression` are balanced.
    Support (), [], {}. Return True if balanced, False otherwise."""
    stack = Stack[str]()
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in pairs:               # opening bracket
            stack.push(char)
        elif char in pairs.values():    # closing bracket
            if stack.is_empty() or pairs[stack.pop()] != char:
                return False

    return stack.is_empty()


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Generic Data Structures ===")

    print("\nTesting Stack with integers:")
    int_stack = Stack[int]()
    int_stack.push(10)
    int_stack.push(20)
    int_stack.push(30)
    print(f"Stack contents (top to bottom): {list(int_stack)}")
    print(f"Popped: {int_stack.pop()}")
    print(f"Popped: {int_stack.pop()}")
    print(f"Stack size: {len(int_stack)}")

    print("\nTesting with custom Point class:")
    point_stack = Stack[Point]()
    point_stack.push(Point(1.0, 2.0))
    point_stack.push(Point(3.0, 4.0))
    print(f"Point stack: {[str(p) for p in point_stack]}")

    print("\nBracket Balance Checker:")
    for expr in ["((()))", "([{}])", "([)]", "", "((("]:
        print(f'"{expr}" → {is_balanced(expr)}')
