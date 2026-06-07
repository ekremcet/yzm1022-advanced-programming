# Lab Session 5: Recursion, Dynamic Programming, and Generics

**Course:** YZM1022 - Advanced Programming  
**Date:** 26.05.2026  
**Duration:** 1 hour (60 Minutes)

---

## Instructions

- This lab consists of **3 questions**, each submitted as a separate Python file.
- You must submit: `q1_recursion.py`, `q2_dynamic.py`, `q3_generics.py`
- Each file must be **self-contained** and runnable: `python3 q1_recursion.py`
- Implement each function/class marked `# YOUR CODE HERE`. A test block is already written
  at the bottom of every file - **do not modify it**; it prints the expected output.
- You may use only the Python standard library (no pip packages).

---

## Grading

| Question  | Topic                          | Points  |
| --------- | ------------------------------ | ------- |
| Q1        | Recursion and Memoization      | 30      |
| Q2        | Dynamic Programming            | 30      |
| Q3        | Generic Programming            | 40      |
| **Total** |                                | **100** |

---

## Question 1: Recursion and Memoization (30 pts)

**Topics:** Recursion, base cases, memoization (Week 11)

Implement the Fibonacci sequence two ways:

- `fibonacci_naive(n)` - nth Fibonacci number with plain recursion and no caching
  (base cases: `fib(0) = 0`, `fib(1) = 1`).
- `fibonacci_memoized(n, memo=None)` - same result, but cache already-computed values in a
  dictionary so each one is only computed once.

The test block then times `fibonacci_naive(35)` against `fibonacci_memoized(35)` to show
why memoization matters.

### Expected Output

```
=== Recursion and Memoization ===
fibonacci_naive(10) = 55
fibonacci_memoized(10) = 55

Timing Fibonacci(35):
  naive:    1.0278s
  memoized: 0.000031s
  speedup:  32907x faster
```

*(Timing numbers and the exact speedup will vary on your machine - that is expected.)*

---

## Question 2: Dynamic Programming - 0/1 Knapsack (30 pts)

**Topics:** DP table, bottom-up approach (Week 11)

Implement one function:

```
knapsack(capacity, items) -> (max_value, dp_table)
```

- `items` is a list of `(weight, value)` tuples.
- `capacity` is the maximum total weight the knapsack can hold.
- Build a table where `dp_table[i][w]` = the best total value using the **first `i` items**
  with a knapsack of capacity `w`. The table has `len(items) + 1` rows and `capacity + 1`
  columns, all starting at 0.
- For each item, you either **skip it** (copy the value from the row above) or **take it**
  (if it fits: `value + dp_table[i-1][w - weight]`). Keep whichever is larger.
- Return the maximum value (`dp_table[n][capacity]`) and the full table.

> You only need the maximum value and the table - you do **not** need to reconstruct
> which items were chosen.

### Expected Output

```
=== 0/1 Knapsack (Dynamic Programming) ===
Items (weight, value): [(2, 3), (3, 4), (4, 5), (5, 6)]
Capacity: 5

DP table (rows = first i items, cols = capacity 0..C):
     0    0    0    0    0    0
     0    0    3    3    3    3
     0    0    3    4    4    7
     0    0    3    4    5    7
     0    0    3    4    5    7

Maximum value: 7
```

---

## Question 3: Generic Programming (40 pts)

**Topics:** Type hints, generics, `TypeVar`, dunder methods (Week 12)

Implement a generic class `SortedList[T]` that always keeps its items in sorted order.
Start with `T = TypeVar("T")` and `class SortedList(Generic[T]):`.

Methods to implement:

- `add(item)` - insert `item` into the correct sorted position. **Hint:** `bisect.insort`.
- `__contains__(item)` - support the `in` operator (membership test).
- `__len__()` - number of items.
- `__iter__()` - iterate over items in sorted order.
- `__repr__()` - return `"SortedList([...])"`.

It must work for any comparable type (e.g. `int` and `str`).

### Expected Output

```
=== Generic SortedList ===
SortedList[int]:
  SortedList([1, 2, 5, 8, 9])
  length: 5
  contains 5: True
  contains 3: False

SortedList[str]:
  SortedList(['apple', 'banana', 'cherry'])
  as list: ['apple', 'banana', 'cherry']
```

---

## Submission

Submit a `.zip` file containing:

```
lab-session-5/
├── q1_recursion.py
├── q2_dynamic.py
└── q3_generics.py
```

Each file must run independently: `python3 qX_filename.py`

**Good luck!**
