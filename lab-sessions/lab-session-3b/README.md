# Lab Session 3B: Pythonic Programming, SOLID, and Testing

**Course:** YZM1022 - Advanced Programming  
**Date:** 28.04.2026  
**Duration:** 1 hour (60 Minutes)

---

## Instructions

- This lab consists of **3 questions**, each submitted as a separate Python file.
- You must submit: `q1_pythonic.py`, `q2_solid.py`, `q3_testing.py`
- Each file must be **self-contained** and runnable: `python3 q1_pythonic.py`
- Your code will be tested by running it - make sure the output matches the expected format.
- You may use only the Python standard library (no pip packages).

---

## Grading

| Question  | Topic                                  | Points  |
| --------- | -------------------------------------- | ------- |
| Q1        | Pythonic Programming                   | 30      |
| Q2        | SOLID Principles — Refactoring         | 30      |
| Q3        | Testing with pytest                    | 40      |
| **Total** |                                        | **100** |

---

## Question 1: Text Analytics Processor (30 pts)

**Topics:** Comprehensions, Generators, Context Managers, Custom Exceptions (Week 6)

### Task

Process text data using Pythonic Python idioms.

### `WordError(Exception)`:
- Custom exception raised when text is empty or None

### `TextProcessor` class:
- `word_count(text: str) -> dict` — **dict comprehension** → `{word: count}` for all words (case-insensitive, split by whitespace)
- `unique_words(text: str) -> set` — **set comprehension** → set of unique words (case-insensitive)
- `filter_by_length(text: str, min_len: int)` — **generator** (use `yield`) that yields words with length >= min_len
- `top_words(text: str, n=5) -> list` — returns top N words by frequency (use `sorted` with `key` parameter)
- `process_file(filename: str)` — **context manager usage**: write text to file, then read it back and return content

### Expected Output

```
=== Text Analytics Processor ===

Original text: The quick brown fox jumps over the lazy dog. The fox is quick.

Word counts:
{'the': 3, 'quick': 2, 'fox': 2, 'brown': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog.': 1, 'is': 1}

Unique words (9 total):
{'brown', 'dog.', 'fox', 'is', 'jumps', 'lazy', 'over', 'quick', 'the'}

Words with 4+ characters:
quick, brown, jumps, over, lazy, dog., quick

Top 3 words by frequency:
1. the (3)
2. quick (2)
3. fox (2)

File processing test:
File content: Hello world from file!

Exception test:
Error caught: Text cannot be empty or None
```

---

## Question 2: Order Management SOLID Refactoring (30 pts)

**Topics:** SRP, OCP, Dependency Inversion (Week 7)

### Task

The following `OrderProcessor` class violates SOLID principles. Refactor it into separate, focused classes.

```python
# BADLY DESIGNED — violates SRP and OCP
class OrderProcessor:
    def __init__(self):
        self.orders = []

    def process_order(self, customer, items, total):
        # validation mixed with business logic (violates SRP)
        if not customer or not items or total <= 0:
            raise ValueError("Invalid order data")
        
        order = {"customer": customer, "items": items, "total": total, "status": "processed"}
        self.orders.append(order)
        
        # email sending mixed with order processing (violates SRP)
        print(f"Email sent to {customer}: Your order for ${total} is confirmed")
        
        # reporting mixed with order processing (violates SRP)
        return f"Order #{len(self.orders)} processed for {customer}"
```

### Refactored classes:

### `OrderValidator`:
- `validate(customer: str, items: list, total: float) -> bool` — returns True if all valid
- `validate_or_raise(customer: str, items: list, total: float)` — raises `ValueError` with descriptive message if invalid

### `OrderRepository`:
- `add(order: dict)` — stores order with auto-generated ID
- `find(order_id: int) -> dict` — returns order or None
- `count() -> int` — returns total number of orders

### `NotificationService`:
- `send_confirmation(customer: str, total: float)` — prints confirmation message

### `OrderReportService`:
- `generate_summary(repo: OrderRepository) -> str` — returns formatted summary

### `OrderProcessor` (refactored):
- Constructor: `OrderProcessor(repo, validator, notifier)` — dependency injection
- `process_order(customer, items, total) -> str` — validates, creates order, sends notification, returns confirmation

### Expected Output

```
=== Order Management SOLID Refactoring ===

Processing valid order...
Email sent to Alice: Your order for $99.99 is confirmed
Order #1 processed for Alice

Processing another order...
Email sent to Bob: Your order for $149.50 is confirmed
Order #2 processed for Bob

Order summary:
Total orders: 2
Average order value: $124.75

Processing invalid order...
Error: Invalid order: customer cannot be empty
```

---

## Question 3: Calculator Testing with pytest (40 pts)

**Topics:** pytest, fixtures, parametrize, exception testing (Week 7)

### Task

Write a test suite for the provided `Calculator` class using `pytest`. Implement at least **10 test cases** (individual assertions or parametrized rows each count).

```python
# PROVIDED — do not modify
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base, exponent):
        if exponent < 0:
            raise ValueError("Exponent cannot be negative")
        return base ** exponent
    
    def sqrt(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of negative number")
        return x ** 0.5
    
    def factorial(self, n):
        if n < 0:
            raise ValueError("Cannot calculate factorial of negative number")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
```

### Requirements:
- Use `@pytest.fixture` to provide a `Calculator` instance
- Use `pytest.raises` to test at least two exception cases (e.g. divide by zero, negative sqrt)
- Cover at least 4 of the 7 methods
- `@pytest.mark.parametrize` is optional but encouraged for methods like `add` or `divide`
- At least 10 test cases total

### Expected Output

```
=== Running Calculator Tests ===

collected 10+ items

PASSED test_add_normal
PASSED test_subtract_normal
PASSED test_multiply_normal
PASSED test_divide_normal
PASSED test_divide_by_zero_raises
PASSED test_power_normal
PASSED test_sqrt_normal
PASSED test_sqrt_negative_raises
PASSED test_factorial_normal
PASSED test_factorial_negative_raises

10 passed in 0.01s

=== All tests passed! ===
```

---

## Submission

Submit a `.zip` file containing:

```
lab-session-3b/
├── q1_pythonic.py
├── q2_solid.py
└── q3_testing.py
```

Q1 and Q2 run as: `python3 qX_filename.py`
Q3 runs as: `pytest q3_testing.py -v`

**Good luck!**