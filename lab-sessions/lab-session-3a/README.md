# Lab Session 3A: Pythonic Programming, SOLID, and Testing

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

| Question  | Topic                          | Points  |
| --------- | ------------------------------ | ------- |
| Q1        | Pythonic Programming           | 30      |
| Q2        | SOLID Principles — Refactoring | 30      |
| Q3        | Testing with pytest            | 40      |
| **Total** |                                | **100** |

---

## Question 1: Student Data Processor (30 pts)

**Topics:** Comprehensions, Generators, Context Managers, Custom Exceptions (Week 6)

### Task

Process a list of student records using Pythonic Python idioms.

### `InvalidGradeError(Exception)`:

- Custom exception raised when a grade is outside 0-100

### `validate_grade(grade: float)`:

- Raises `InvalidGradeError` if grade < 0 or grade > 100

### `StudentProcessor` class:

- `passing_students(students)` — **generator** (use `yield`) that yields students with average grade ≥ 60
- `grade_summary(students)` — **dict comprehension** → `{name: average_grade}` for all students
- `top_students(students, n=3)` — returns top N students by average grade (use `sorted` with `key`)
- `course_averages(students)` — **dict comprehension** → `{course: average}` across all students

### `ReportWriter` — context manager:

- `__init__(filename)`, `__enter__()` opens file and returns self, `__exit__()` closes and prints confirmation
- `write(text)` — writes a line

### Expected Output

```
=== Student Data Processor ===

Passing students (avg >= 60):
  Alice: 82.33
  Bob: 73.67
  Carol: 91.00

Grade summary:
  Alice: 82.33
  Bob: 73.67
  Carol: 91.00
  Dave: 45.33

Course averages:
  Math: 72.75
  Physics: 73.50
  Programming: 73.00

Top 2 students:
  1. Carol - 91.00
  2. Alice - 82.33

Writing report...
Report saved to: grades.txt

Validation test:
Error caught: Grade 110 is out of range (0-100)
```

---

## Question 2: Refactoring with SOLID (30 pts)

**Topics:** SRP, OCP, Dependency Inversion (Week 7)

### Task

The following `UserManager` class violates SOLID principles. Refactor it into separate, focused classes.

```python
# BADLY DESIGNED — violates SRP and OCP
class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        if "@" not in email:
            raise ValueError("Invalid email")
        self.users.append({"name": name, "email": email})
        # sends email directly (violates SRP)
        print(f"Sending welcome email to {email}")

    def get_user(self, name):
        for u in self.users:
            if u["name"] == name:
                return u
        return None

    def generate_report(self):
        # reporting mixed with user management (violates SRP)
        return "\n".join(f"{u['name']}: {u['email']}" for u in self.users)
```

### Refactored classes:

### `EmailValidator`:

- `validate(email: str) -> bool` — returns True if email contains "@"
- `validate_or_raise(email: str)` — raises `ValueError` if invalid

### `EmailService`:

- `send_welcome(email: str)` — prints `"Sending welcome email to {email}"`

### `UserRepository`:

- `add(name: str, email: str)` — stores user dict `{"name": ..., "email": ...}`
- `find(name: str)` — returns user dict or None
- `all() -> list` — returns all users

### `UserReportService`:

- `generate(repo: UserRepository) -> str` — returns formatted report

### `UserManager` (refactored):

- Constructor: `UserManager(repo, validator, email_service)` — dependency injection
- `add_user(name, email)` — validates, adds, sends welcome
- `get_user(name)` — delegates to repo
- `generate_report()` — delegates to report service

### Expected Output

```
=== SOLID Refactoring ===
Sending welcome email to alice@example.com
Sending welcome email to bob@example.com

Users:
  alice@example.com
  bob@example.com

Total users: 2

Error: Invalid email format
```

---

## Question 3: Unit Testing with pytest (40 pts)

**Topics:** pytest, fixtures, parametrize, exception testing (Week 7)

### Task

Write a test suite for the provided `BankAccount` class using `pytest`. Implement at least **10 test cases** (individual assertions or parametrized rows each count).

```python
# PROVIDED — do not modify
class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        return self._balance

    def transfer(self, other: 'BankAccount', amount: float):
        self.withdraw(amount)
        other.deposit(amount)
```

### Requirements:

- Use `@pytest.fixture` to provide a pre-funded account (e.g. balance=1000)
- Use `pytest.raises` to assert exceptions on invalid operations
- Cover: init, deposit, withdraw, transfer — at least one error case per operation
- `@pytest.mark.parametrize` is optional but encouraged

### Expected Output

```
=== Running BankAccount Tests ===

collected 10+ items

PASSED test_initial_balance
PASSED test_negative_initial_raises
PASSED test_deposit_increases_balance
PASSED test_deposit_invalid_raises
PASSED test_withdraw_valid
PASSED test_withdraw_insufficient_raises
PASSED test_withdraw_invalid_raises
PASSED test_transfer_updates_both_balances
PASSED test_transfer_insufficient_raises
PASSED test_multiple_sequential_operations

10 passed in 0.01s

=== All tests passed! ===
```

---

## Submission

Submit a `.zip` file containing:

```
lab-session-3a/
├── q1_pythonic.py
├── q2_solid.py
└── q3_testing.py
```

Q1 and Q2 run as: `python3 qX_filename.py`
Q3 runs as: `pytest q3_testing.py -v`

**Good luck!**
