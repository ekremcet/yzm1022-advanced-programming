"""
Lab Session 5 - Question 3: Generic Programming - SOLUTION
YZM1022 Advanced Programming
"""

from typing import TypeVar, Generic, Iterator, List
import bisect

T = TypeVar("T")


class SortedList(Generic[T]):
    """A generic list that always keeps its items in sorted order."""

    def __init__(self):
        self._items: List[T] = []

    def add(self, item: T) -> None:
        """Insert item into its correct sorted position."""
        bisect.insort(self._items, item)

    def __contains__(self, item: T) -> bool:
        """Efficient membership test using binary search."""
        i = bisect.bisect_left(self._items, item)
        return i < len(self._items) and self._items[i] == item

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __repr__(self) -> str:
        return f"SortedList({self._items})"


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
