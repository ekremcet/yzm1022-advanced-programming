# Lab Session 4A: Functional Programming

**Course:** YZM1022 - Advanced Programming  
**Date:** 12.05.2026  
**Duration:** 1 hour (60 Minutes)

---

## Instructions

- This lab consists of **3 questions**, each submitted as a separate Python file.
- You must submit: `q1_pure_functions.py`, `q2_immutability.py`, `q3_pipeline.py`
- Each file must be **self-contained** and runnable: `python3 q1_pure_functions.py`
- Your code will be tested by running it - make sure the output matches the expected format.
- You may use only the Python standard library (no pip packages).

---

## Grading

| Question  | Topic                          | Points  |
| --------- | ------------------------------ | ------- |
| Q1        | Pure Functions                 | 30      |
| Q2        | Immutable Data Transformations | 30      |
| Q3        | Functional Data Pipeline       | 40      |
| **Total** |                                | **100** |

---

## Question 1: Pure Functions (30 pts)

**Topics:** Pure functions, side effects, immutability (Week 9)

### Task

Three impure functions are shown in the starter file. Rewrite each as a **pure** version:

- `calculate_price_pure(original_price: float, discount: float) -> float` — no global variable; discount passed as parameter
- `normalize_tags_pure(tags: list) -> list` — return a new list; never modify the input
- `get_age_category_pure(birth_year: int, current_year: int) -> str` — no `datetime.now()`; year passed as parameter

### Expected Output

```
=== Pure Functions ===

--- 1a: Price Calculator ---
$100.00 with 20% discount: $80.00
$50.00  with 10% discount: $45.00

--- 1b: Tag Normalizer ---
Output:             ['python', 'java', 'rust']
Original unchanged: ['  Python  ', 'JAVA', '  rust']

--- 1c: Age Category ---
Born 2010, year 2024: minor
Born 2000, year 2024: adult
Born 1950, year 2024: senior
```

---

## Question 2: Immutable Data Transformations (30 pts)

**Topics:** Dict spreading, immutability pattern (Week 9)

### Task

Implement two functions that return brand-new dicts without touching the input:

- `apply_discount(product: dict, percent: float) -> dict` — return a new dict with `price` reduced by `percent`%
- `mark_out_of_stock(product: dict) -> dict` — return a new dict with `in_stock` set to `False`

**Useful pattern:** `{**original, "key": new_value}` copies all fields and overrides one.

### Expected Output

```
=== Immutable Data Transformations ===

apply_discount(Laptop, 10%):
  New price:       $1080.00
  Original price:  $1200.00  (must be unchanged)

mark_out_of_stock(Book):
  New in_stock:      False
  Original in_stock: True   (must be unchanged)

In-stock Electronics after 15% discount:
  Laptop: $1020.00
  Webcam: $51.00

Original prices unchanged:
  Laptop: $1200.00
  Book: $15.00
  Headphones: $80.00
  Notebook: $5.00
  Webcam: $60.00
```

---

## Question 3: Functional Data Pipeline (40 pts)

**Topics:** Comprehensions, map, filter, reduce, lambda (Week 9)

### Task

The `orders` list is already defined in the starter file. Write five **expressions** (no `for` loops with `append`) and assign each to the variable name shown:

- `revenue` — total of completed orders after 5% discount → **446.5**
- `completed_customers` — sorted list of unique customer names with completed orders → **['Alice', 'Bob', 'Charlie']**
- `largest_order` — the order dict with the most items → **Charlie's order (id=3)**
- `all_pending_small` — `True` if ALL pending orders have total < 100 → **True**
- `spending` — dict mapping each customer to their total spend across all statuses

**Allowed:** list/generator comprehensions, `map()`, `filter()`, `sum()`, `max()`, `min()`, `sorted()`, `any()`, `all()`, `reduce()`  
**Not allowed:** `result = []; for ...: result.append(...)`

### Expected Output

```
=== Functional Data Pipeline ===

Revenue (completed, 5% discount): $446.50
Completed customers:              ['Alice', 'Bob', 'Charlie']
Largest order:                    id=3, customer=Charlie
All pending orders under $100:    True

Total spend per customer:
  Alice: $200.00
  Bob: $200.00
  Charlie: $200.00
  Diana: $95.00
```

---

## Submission

Submit a `.zip` file containing:

```
lab-session-4a/
├── q1_pure_functions.py
├── q2_immutability.py
└── q3_pipeline.py
```

Each file must run independently: `python3 qX_filename.py`

**Good luck!**
