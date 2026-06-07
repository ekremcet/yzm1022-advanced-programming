"""
Lab Session 5 - Question 1: Recursion and Memoization (30 pts)
See README.md for the full description.

Implement each function marked `# YOUR CODE HERE`.
Do NOT modify the test block at the bottom - it prints the expected output.
"""

import time


def fibonacci_naive(n):
    """nth Fibonacci number with plain recursion (no caching).
    Base cases: fib(0) = 0, fib(1) = 1."""
    # YOUR CODE HERE
    pass


def fibonacci_memoized(n, memo=None):
    """nth Fibonacci number, caching results in a dict so each value is
    only computed once."""
    # YOUR CODE HERE
    pass


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Recursion and Memoization ===")

    print(f"fibonacci_naive(10) = {fibonacci_naive(10)}")
    print(f"fibonacci_memoized(10) = {fibonacci_memoized(10)}")

    print("\nTiming Fibonacci(35):")
    start = time.time()
    fibonacci_naive(35)
    naive_time = time.time() - start

    start = time.time()
    fibonacci_memoized(35)
    memo_time = time.time() - start

    print(f"  naive:    {naive_time:.4f}s")
    print(f"  memoized: {memo_time:.6f}s")
    print(f"  speedup:  {naive_time / memo_time:.0f}x faster")
