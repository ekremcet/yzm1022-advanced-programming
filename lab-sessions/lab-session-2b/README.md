# Lab Session 2B - Design Patterns

**Course:** YZM1022 - Advanced Programming  
**Date:** 07.04.2026  
**Duration:** 1 hour (60 Minutes)

---

## Instructions

- This lab consists of **3 questions**, each submitted as a separate Python file.
- You must submit: `q1_builder.py`, `q2_adapter.py`, `q3_strategy.py`
- Each file must be **self-contained** and runnable: `python3 q1_builder.py`
- Your code will be tested by running it - make sure the output matches the expected format.
- You may use only the Python standard library (no pip packages).

---

## Grading

| Question  | Topic            | Points  |
| --------- | ---------------- | ------- |
| Q1        | Builder Pattern  | 30      |
| Q2        | Adapter Pattern  | 30      |
| Q3        | Strategy Pattern | 40      |
| **Total** |                  | **100** |

---

## Question 1: Pizza Order Builder (30 pts)

**Topics:** Builder Pattern (Week 4)

### Task

Build a pizza ordering system using the Builder pattern.

### `Pizza` class — product:

- **Attributes:** `size` (str), `crust` (str), `sauce` (str), `toppings` (list), `extra_cheese` (bool)
- **Method:** `__str__()` -> formatted pizza description (see expected output)

### `PizzaBuilder` — builder:

- **Method:** `set_size(size: str)` -> returns self for chaining
- **Method:** `set_crust(crust: str)` -> returns self for chaining
- **Method:** `set_sauce(sauce: str)` -> returns self for chaining
- **Method:** `add_topping(topping: str)` -> returns self for chaining
- **Method:** `extra_cheese()` -> sets extra_cheese=True, returns self for chaining
- **Method:** `build() -> Pizza` -> creates and returns Pizza instance. Raises `ValueError` if size not set.

### Expected Output

```
=== Pizza Order Builder ===

Building pizzas using builder pattern...

Pizza 1: Large Thin Crust pizza with Marinara sauce
Toppings: Pepperoni, Mushrooms
Extra cheese: Yes

Pizza 2: Medium Thick Crust pizza with BBQ sauce
Toppings: Chicken, Onions, Bell peppers
Extra cheese: No

Pizza 3: Small Hand-tossed pizza with White sauce
Toppings: Spinach
Extra cheese: Yes
```

---

## Question 2: Payment Adapter (30 pts)

**Topics:** Adapter Pattern (Week 5)

### Task

Integrate a legacy payment system with a modern API using the Adapter pattern.

### `LegacyPaymentSystem` — legacy system (given):

- **Method:** `make_payment(amount: float, account: str) -> str` -> returns `"Payment of ${amount} charged to account {account}"`
- **Method:** `check_balance(account: str) -> float` -> returns mock balance (use `account_balance = {"12345": 1000.0, "67890": 500.0}`)

### `ModernPaymentAPI(ABC)` — target interface:

- **Abstract method:** `pay(amount: float) -> bool` -> returns True if payment successful
- **Abstract method:** `get_balance() -> float` -> returns current balance

### `PaymentAdapter(ModernPaymentAPI)` — adapter:

- **Constructor:** takes a `LegacyPaymentSystem` instance and account number
- **Method:** `pay(amount: float)` -> uses legacy system's `make_payment`, prints result, returns True
- **Method:** `get_balance()` -> uses legacy system's `check_balance`

### `OnlineStore` — client:

- **Constructor:** takes a `ModernPaymentAPI` instance (dependency injection)
- **Method:** `buy(item: str, price: float) -> str` -> checks balance, attempts payment, returns result message

### Expected Output

```
=== Payment Adapter ===

Alice's initial balance: $1000.00

Buying laptop for $800.00...
Payment of $800.0 charged to account 12345
Purchase successful: laptop

Alice's remaining balance: $1000.00

Bob's initial balance: $500.00

Buying expensive watch for $600.00...
Insufficient funds for expensive watch (need $600.00, have $500.00)

Bob's remaining balance: $500.00
```

---

## Question 3: Sorting Strategy (40 pts)

**Topics:** Strategy Pattern (Week 5)

### Task

Implement different sorting algorithms using the Strategy pattern and compare their performance.

### `SortStrategy(ABC)` — strategy interface:

- **Abstract method:** `sort(data: list) -> list` -> returns sorted copy of data
- **Attribute:** `comparisons` (int) -> tracks number of comparisons made

### `BubbleSort(SortStrategy)` — concrete strategy:

- Implements O(n²) bubble sort algorithm
- Counts comparisons during sorting

### `MergeSort(SortStrategy)` — concrete strategy:

- Implements recursive merge sort algorithm
- Counts comparisons during sorting

### `QuickSort(SortStrategy)` — concrete strategy:

- Implements quicksort with first element as pivot
- Counts comparisons during sorting

### `Sorter` — context:

- **Constructor:** takes a `SortStrategy` instance (dependency injection)
- **Method:** `sort(data: list) -> list` -> delegates to strategy
- **Method:** `compare_strategies(data: list) -> dict` -> tests all three strategies on the same data, returns `{strategy_name: (sorted_result, comparisons, time_ms)}`

### Expected Output

```
=== Sorting Strategy ===

Original data: [64, 34, 25, 12, 22, 11, 90]

Using Bubble Sort:
Sorted: [11, 12, 22, 25, 34, 64, 90]
Comparisons: 21

Using Merge Sort:
Sorted: [11, 12, 22, 25, 34, 64, 90]
Comparisons: 13

Using Quick Sort:
Sorted: [11, 12, 22, 25, 34, 64, 90]
Comparisons: 12

Strategy Comparison Results:
BubbleSort: 21 comparisons, 0.001ms
MergeSort: 13 comparisons, 0.001ms
QuickSort: 12 comparisons, 0.001ms
```

---

## Submission

Submit a `.zip` file containing:

```
lab-session-2b/
├── q1_builder.py
├── q2_adapter.py
└── q3_strategy.py
```

Each file must run independently: `python3 qX_filename.py`

**Good luck!**
