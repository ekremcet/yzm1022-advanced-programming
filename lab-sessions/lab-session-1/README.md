# Lab Session 1: OOP Fundamentals

**Course:** YZM1022 - Advanced Programming  
**Date:** 31.03.2026  
**Duration:** 1 hour (60 Minutes)

---

## Instructions

- This lab consists of **3 questions**, each submitted as a separate Python file.
- You must submit: `q1_library.py`, `q2_vehicles.py`, `q3_restaurant.py`
- Each file must be **self-contained** and runnable: `python3 q1_library.py`
- Your code will be tested by running it - make sure the output matches the expected format.
- You may use only the Python standard library (no pip packages).

---

## Grading

| Question  | Topic                                               | Points  |
| --------- | --------------------------------------------------- | ------- |
| Q1        | Classes, Encapsulation, Properties, Special Methods | 30      |
| Q2        | Inheritance, Polymorphism, Abstract Classes         | 30      |
| Q3        | Composition, Interfaces, Dependency Injection       | 40      |
| **Total** |                                                     | **100** |

---

## Question 1: Library Management System (30 pts)

**Topics:** Classes, Encapsulation, Properties, Special Methods

### Task

Create a library management system with the following classes:

### `Book` class:

- **Attributes:** `title` (str), `author` (str), `isbn` (str), `_copies` (int, private)
- **Property:** `copies` - getter returns `_copies`, setter validates that value ≥ 0 (raise `ValueError` if negative)
- **Method:** `__str__()` -> `"Book(title='...', author='...', isbn='...', copies=N)"`
- **Method:** `__eq__(other)` -> Two books are equal if they have the same ISBN

### `Member` class:

- **Attributes:** `name` (str), `member_id` (str), `_borrowed_books` (list, private, default empty)
- **Property:** `borrowed_books` -> returns a **copy** of `_borrowed_books`
- **Method:** `borrow(book)` -> adds book to borrowed list, decrements book's copies. Raise `ValueError` if no copies available.
- **Method:** `return_book(book)` -> removes book from borrowed list, increments book's copies. Raise `ValueError` if book not borrowed.
- **Method:** `__str__()` -> `"Member(name='...', id='...', borrowed=N)"`

### `Library` class:

- **Attributes:** `name` (str), `_books` (dict: isbn -> Book), `_members` (dict: member_id -> Member)
- **Methods:** `add_book(book)`, `register_member(member)`, `find_book(isbn)` -> Book or None, `get_member(member_id)` -> Member or None
- **Method:** `__len__()` -> returns total number of unique books
- **Method:** `__contains__(isbn)` -> returns True if book with that ISBN exists

### Expected Output

```
=== Library Management System ===
Library: YTU Central Library
Books: 3
Members: 2

Alice borrows 'Clean Code'...
Alice's borrowed books: 1
Clean Code copies remaining: 2

Bob borrows 'Clean Code'...
Clean Code copies remaining: 1

Alice returns 'Clean Code'...
Clean Code copies remaining: 2

Book equality test: True (same ISBN)
Book in library: True
Library size: 3
```

---

## Question 2: Vehicle Fleet System (30 pts)

**Topics:** Inheritance, Polymorphism, ABC, Method Overriding, isinstance

### Task

Create a vehicle fleet management system using abstract classes and inheritance.

### `Vehicle(ABC)` - Abstract base class:

- **Attributes:** `brand` (str), `model` (str), `year` (int), `_mileage` (float, starts at 0)
- **Abstract method:** `fuel_cost(distance: float) -> float` - cost to travel given distance
- **Abstract property:** `vehicle_type` -> returns a string (e.g., "Car", "Truck")
- **Concrete method:** `drive(distance: float)` -> adds distance to mileage, prints `"  {vehicle_type} drove {distance} km"`
- **Concrete method:** `__str__()` -> `"  {year} {brand} {model} ({vehicle_type}) - {mileage} km"`
- **Property:** `mileage` -> getter only (no setter - mileage only increases via drive())

### `Car(Vehicle)`:

- Extra attribute: `fuel_efficiency` (km per liter, default 15.0)
- `fuel_cost(distance)` = `distance / fuel_efficiency * 7.5` (fuel price per liter)
- `vehicle_type` = "Car"

### `ElectricCar(Car)`:

- Override `fuel_cost(distance)` = `distance * 0.15 * 3.0` (kWh per km \* electricity price)
- `vehicle_type` = "Electric Car"

### `Truck(Vehicle)`:

- Extra attribute: `cargo_capacity` (tons)
- `fuel_cost(distance)` = `distance / 5.0 * 7.5`
- `vehicle_type` = "Truck"
- Extra method: `load(weight: float)` -> print message, raise `ValueError` if weight > cargo_capacity

### `Fleet` class:

- Stores a list of vehicles
- **Method:** `add_vehicle(vehicle: Vehicle)` - type check with isinstance
- **Method:** `total_fuel_cost(distance: float) -> float` - sum of fuel costs for all vehicles
- **Method:** `get_by_type(vehicle_type: str) -> list` - filter vehicles by type
- **Method:** `__len__()`, `__iter__()` - fleet is iterable

### Expected Output

```
=== Vehicle Fleet System ===
Fleet size: 4

All vehicles:
  2024 Toyota Corolla (Car) - 0 km
  2024 Tesla Model3 (Electric Car) - 0 km
  2024 Volvo FH16 (Truck) - 0 km
  2023 Ford Transit (Truck) - 0 km

Driving all vehicles 100 km...
  Car drove 100 km
  Electric Car drove 100 km
  Truck drove 100 km
  Truck drove 100 km

Fuel costs for 500 km trip:
  Toyota Corolla: $250.00
  Tesla Model3: $225.00
  Volvo FH16: $750.00
  Ford Transit: $750.00
  Total fleet cost: $1975.00

Cars in fleet: 2
Trucks in fleet: 2
```

---

## Question 3: Restaurant Order System (40 pts)

**Topics:** Composition, Interfaces (ABC), Dependency Injection

### Task

Build a restaurant ordering system using composition and dependency injection.

### `MenuItem` class:

- **Attributes:** `name` (str), `price` (float), `category` (str: "food", "drink", "dessert")
- **Method:** `__str__()` -> `"{name} (${price:.2f})"`

### `PaymentMethod(ABC)` - Interface:

- **Abstract method:** `process_payment(amount: float) -> str`
- **Abstract property:** `method_name -> str`

### `CreditCardPayment(PaymentMethod)`:

- Attribute: `card_number` (str)
- `process_payment(amount)` -> `"Charged ${amount:.2f} to card ending {last 4 digits}"`
- `method_name` = "Credit Card"

### `CashPayment(PaymentMethod)`:

- `process_payment(amount)` -> `"Received ${amount:.2f} in cash"`
- `method_name` = "Cash"

### `DiscountStrategy(ABC)` - Interface:

- **Abstract method:** `apply_discount(total: float) -> float` - returns discounted total
- **Abstract property:** `description -> str`

### `PercentageDiscount(DiscountStrategy)`:

- Attribute: `percentage` (float, 0-100)
- Returns `total * (1 - percentage/100)`

### `FixedDiscount(DiscountStrategy)`:

- Attribute: `amount` (float)
- Returns `max(0, total - amount)`

### `Order` - uses composition and DI:

- **Constructor:** `Order(table_number: int, payment: PaymentMethod, discount: DiscountStrategy = None)`
- **Method:** `add_item(item: MenuItem)` -> adds to order
- **Method:** `remove_item(item_name: str)` -> removes first item matching name
- **Property:** `subtotal -> float` - sum of item prices
- **Property:** `total -> float` - subtotal after discount (if any)
- **Method:** `checkout() -> str` - processes payment via the injected PaymentMethod, returns result string
- **Method:** `__str__()` -> formatted order summary (see expected output)

### Expected Output

```
=== Restaurant Order System ===

--- Order for Table 5 ---
Items:
  1. Burger ($12.99)
  2. Fries ($4.99)
  3. Cola ($2.50)
  4. Cheesecake ($7.99)
Subtotal: $28.47
Discount: 10% off
Total: $25.62
Payment: Credit Card

Processing payment...
Charged $25.62 to card ending 4242

--- Order for Table 3 ---
Items:
  1. Pizza ($15.99)
  2. Water ($1.50)
Subtotal: $17.49
Discount: $5.00 off
Total: $12.49
Payment: Cash

Processing payment...
Received $12.49 in cash
```

---

## Submission

Submit a `.zip` file containing:

```
lab-session-1/
├── q1_library.py
├── q2_vehicles.py
└── q3_restaurant.py
```

Each file must run independently: `python3 qX_filename.py`

**Good luck!**
