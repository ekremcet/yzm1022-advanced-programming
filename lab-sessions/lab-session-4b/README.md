# Lab Session 4B: Functional Programming

**Course:** YZM1022 - Advanced Programming  
**Date:** 12.05.2026  
**Duration:** 1 hour (60 Minutes)

---

## Instructions

- This lab consists of **3 questions**, each submitted as a separate Python file.
- You must submit: `q1_closures.py`, `q2_higher_order.py`, `q3_functools.py`
- Each file must be **self-contained** and runnable: `python3 q1_closures.py`
- Your code will be tested by running it - make sure the output matches the expected format.
- You may use only the Python standard library (no pip packages).

---

## Grading

| Question  | Topic                          | Points  |
| --------- | ------------------------------ | ------- |
| Q1        | Closures and Function Factories | 30      |
| Q2        | Higher-Order Functions         | 30      |
| Q3        | functools                      | 40      |
| **Total** |                                | **100** |

---

## Question 1: Closures and Function Factories (30 pts)

**Topics:** Closures, function factories, immutability (Week 10)

### Task

Implement three **function factories** — functions that create and return other functions.

- `make_raise_calculator(percent)` — returns a function `employee_dict → new employee_dict` with salary raised by `percent`% (use `int()` to truncate). Must **not** modify the input dict.
- `make_department_filter(department)` — returns a predicate `employee_dict → bool`, True when department matches.
- `make_salary_total(department)` — returns a function `list[employee_dict] → int`, total salary for that department.

### Expected Output

```
=== Closures and Function Factories ===

After 10% raise:
  Alice Johnson: $75000 → $82500
  Bob Smith: $45000 → $49500
  Carol Brown: $82000 → $90200
  David Wilson: $52000 → $57200
  Eva Davis: $68000 → $74800
  Frank Miller: $38000 → $41800

Engineering employees:
  Alice Johnson: $75000
  Carol Brown: $82000
  Eva Davis: $68000

Marketing employees:
  Bob Smith: $45000
  Frank Miller: $38000

Department salary totals:
  Engineering: $225000
  Marketing:   $83000
  Sales:       $52000
```

---

## Question 2: Higher-Order Functions (30 pts)

**Topics:** Functions as arguments and return values (Week 10)

### Task

Implement three general-purpose higher-order utilities:

- `pipeline(*funcs)` — returns a function that applies each `func` in sequence (left to right) to its input
- `apply_to_all(func, items)` — applies `func` to every item; if `func` raises, store `None` for that item; never raises
- `group_by(key_func, items)` — groups items into a dict mapping `key_func(item)` → list of items with that key

### Expected Output

```
=== Higher-Order Functions ===

pipeline(add_tax, apply_discount, to_string):
  100.0 → $106.20
  50.0 → $53.10
  200.0 → $212.40

apply_to_all(safe_sqrt, [4, 9, -1, 16, -4, 25]):
  [2.0, 3.0, None, 4.0, None, 5.0]

group_by(first letter, words):
  'a': ['apple', 'avocado']
  'b': ['banana', 'blueberry']
  'c': ['cherry', 'citrus']
```

---

## Question 3: functools (40 pts)

**Topics:** `functools.partial`, `functools.lru_cache` (Week 10)

### Task

The starter file already defines `power(base, exponent)`. Use `functools` tools to build on it:

- `square` — a partial application of `power` that always raises to the 2nd power
- `cube` — a partial application of `power` that always raises to the 3rd power
- `fibonacci(n)` — recursive Fibonacci decorated with `@lru_cache` so repeated calls are instant

### Expected Output

```
=== functools ===

partial — square and cube:
  square(2) = 4,  cube(2) = 8
  square(3) = 9,  cube(3) = 27
  square(4) = 16,  cube(4) = 64
  square(5) = 25,  cube(5) = 125

lru_cache — fibonacci:
  fib(10) = 55
  fib(20) = 6765
  fib(30) = 832040
  Cache info: CacheInfo(hits=30, misses=31, maxsize=None, currsize=31)
```

---

## Submission

Submit a `.zip` file containing:

```
lab-session-4b/
├── q1_closures.py
├── q2_higher_order.py
└── q3_functools.py
```

Each file must run independently: `python3 qX_filename.py`

**Good luck!**
