"""
Lab Session 5 - Question 3: Generic Programming (40 pts)
See README.md for the full description.

Implement each method marked `# YOUR CODE HERE`.
Do NOT modify the test block at the bottom - it prints the expected output.
"""

from typing import TypeVar, Generic, Iterator, List

T = TypeVar("T")


class SortedList(Generic[T]):
    """A generic list that always keeps its items in sorted order (any comparable type)."""

    def __init__(self):
        # YOUR CODE HERE
        pass

    def add(self, item: T) -> None:
        """Insert item into its correct sorted position (hint: bisect.insort)."""
        # YOUR CODE HERE
        pass

    def __contains__(self, item: T) -> bool:
        """Membership test for the `in` operator."""
        # YOUR CODE HERE
        pass

    def __len__(self) -> int:
        """Number of items."""
        # YOUR CODE HERE
        pass

    def __iter__(self) -> Iterator[T]:
        """Iterate over items in sorted order."""
        # YOUR CODE HERE
        pass

    def __repr__(self) -> str:
        """Return "SortedList([...])"."""
        # YOUR CODE HERE
        pass


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Generic SortedList ===")

    print("SortedList[int]:")
    numbers = SortedList[int]()
    for n in [5, 2, 8, 1, 9]:
        numbers.add(n)
    print(f"  {numbers}")
    print(f"  length: {len(numbers)}")
    print(f"  contains 5: {5 in numbers}")
    print(f"  contains 3: {3 in numbers}")

    print("\nSortedList[str]:")
    words = SortedList[str]()
    for w in ["banana", "apple", "cherry"]:
        words.add(w)
    print(f"  {words}")
    print(f"  as list: {list(words)}")
