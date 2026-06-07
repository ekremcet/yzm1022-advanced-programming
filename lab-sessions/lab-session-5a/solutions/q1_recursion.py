"""
Lab Session 5 - Question 1: Recursion and Memoization - SOLUTION
YZM1022 Advanced Programming
"""

import time


def fibonacci_naive(n):
    """nth Fibonacci number with plain recursion (no caching)."""
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_memoized(n, memo=None):
    """nth Fibonacci number, caching results in a dict so each value is
    only computed once."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
    return memo[n]


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
