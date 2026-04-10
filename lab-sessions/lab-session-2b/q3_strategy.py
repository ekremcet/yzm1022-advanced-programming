"""
Lab Session 2B — Question 3: Sorting Strategy
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
    print("=== Sorting Strategy ===")

    data = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal data: {data}")

    # Test individual strategies
    bubble_sort = BubbleSort()
    merge_sort = MergeSort()
    quick_sort = QuickSort()

    sorter = Sorter(bubble_sort)
    result = sorter.sort(data.copy())
    print(f"\nUsing Bubble Sort:")
    print(f"Sorted: {result}")
    print(f"Comparisons: {bubble_sort.comparisons}")

    sorter = Sorter(merge_sort)
    result = sorter.sort(data.copy())
    print(f"\nUsing Merge Sort:")
    print(f"Sorted: {result}")
    print(f"Comparisons: {merge_sort.comparisons}")

    sorter = Sorter(quick_sort)
    result = sorter.sort(data.copy())
    print(f"\nUsing Quick Sort:")
    print(f"Sorted: {result}")
    print(f"Comparisons: {quick_sort.comparisons}")

    # Compare strategies
    sorter = Sorter(bubble_sort)
    comparison = sorter.compare_strategies(data.copy())
    print(f"\nStrategy Comparison Results:")
    for strategy, (result, comparisons, time_ms) in comparison.items():
        print(f"{strategy}: {comparisons} comparisons, {time_ms:.3f}ms")