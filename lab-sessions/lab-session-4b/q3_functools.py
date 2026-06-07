"""
Lab Session 4B — Question 3: functools (40 pts)
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME:
STUDENT ID:
"""

from functools import partial, lru_cache


def power(base, exponent):
    return base ** exponent

# YOUR CODE HERE
# Use partial and lru_cache as described in README.md


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== functools ===")

    print("\npartial — square and cube:")
    for n in [2, 3, 4, 5]:
        print(f"  square({n}) = {square(n)},  cube({n}) = {cube(n)}")

    print("\nlru_cache — fibonacci:")
    for n in [10, 20, 30]:
        print(f"  fib({n}) = {fibonacci(n)}")
    print(f"  Cache info: {fibonacci.cache_info()}")
