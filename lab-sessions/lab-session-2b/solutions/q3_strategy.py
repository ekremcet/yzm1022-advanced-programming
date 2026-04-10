"""
Lab Session 2B — Question 3: Sorting Strategy
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME: Solution
STUDENT ID: 000000
"""

from abc import ABC, abstractmethod
import time


class SortStrategy(ABC):
    def __init__(self):
        self.comparisons = 0
    
    @abstractmethod
    def sort(self, data):
        pass


class BubbleSort(SortStrategy):
    def sort(self, data):
        self.comparisons = 0
        arr = data.copy()
        n = len(arr)
        
        for i in range(n):
            for j in range(0, n - i - 1):
                self.comparisons += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        return arr


class MergeSort(SortStrategy):
    def sort(self, data):
        self.comparisons = 0
        return self._merge_sort(data.copy())
    
    def _merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self._merge_sort(arr[:mid])
        right = self._merge_sort(arr[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            self.comparisons += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result


class QuickSort(SortStrategy):
    def sort(self, data):
        self.comparisons = 0
        arr = data.copy()
        self._quick_sort(arr, 0, len(arr) - 1)
        return arr
    
    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)
    
    def _partition(self, arr, low, high):
        pivot = arr[low]  # First element as pivot
        i = low + 1
        j = high
        
        while True:
            while i <= j:
                self.comparisons += 1
                if arr[i] > pivot:
                    break
                i += 1
            
            while i <= j:
                self.comparisons += 1
                if arr[j] <= pivot:
                    break
                j -= 1
            
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                break
        
        arr[low], arr[j] = arr[j], arr[low]
        return j


class Sorter:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def sort(self, data):
        return self.strategy.sort(data)
    
    def compare_strategies(self, data):
        strategies = {
            "BubbleSort": BubbleSort(),
            "MergeSort": MergeSort(),
            "QuickSort": QuickSort()
        }
        
        results = {}
        for name, strategy in strategies.items():
            start_time = time.time()
            sorted_result = strategy.sort(data.copy())
            end_time = time.time()
            time_ms = (end_time - start_time) * 1000
            
            results[name] = (sorted_result, strategy.comparisons, time_ms)
        
        return results


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