"""Lab Session 4B — Q3 Solution: functools"""

from functools import partial, lru_cache


def power(base, exponent):
    return base ** exponent


square = partial(power, exponent=2)
cube   = partial(power, exponent=3)


@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


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
