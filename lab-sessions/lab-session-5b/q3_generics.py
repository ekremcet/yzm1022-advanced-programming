"""
Lab Session 5B - Question 3: Generic Data Structures (40 pts)
See README.md for the full description.

Implement each method/function marked `# YOUR CODE HERE`.
Do NOT modify the test block at the bottom - it prints the expected output.
"""

from typing import TypeVar, Generic, Iterator

T = TypeVar("T")


class Stack(Generic[T]):
    """Generic stack that works with any type T."""

    def __init__(self):
        # YOUR CODE HERE
        pass

    def push(self, item: T) -> None:
        """Add item to the top of the stack."""
        # YOUR CODE HERE
        pass

    def pop(self) -> T:
        """Remove and return the top item (raise IndexError if empty)."""
        # YOUR CODE HERE
        pass

    def peek(self) -> T:
        """Return the top item without removing it (raise IndexError if empty)."""
        # YOUR CODE HERE
        pass

    def is_empty(self) -> bool:
        """True if the stack has no items."""
        # YOUR CODE HERE
        pass

    def __len__(self) -> int:
        """Number of items."""
        # YOUR CODE HERE
        pass

    def __iter__(self) -> Iterator[T]:
        """Iterate from top to bottom."""
        # YOUR CODE HERE
        pass


class Point:
    """Custom Point class for demonstrating the stack with a custom type."""

    def __init__(self, x: float, y: float):
        # YOUR CODE HERE
        pass

    def __str__(self) -> str:
        # YOUR CODE HERE  (return "Point(x, y)")
        pass


def is_balanced(expression: str) -> bool:
    """Use your Stack to check whether the brackets in `expression` are balanced.
    Support (), [], {}. Return True if balanced, False otherwise."""
    # YOUR CODE HERE
    pass


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
