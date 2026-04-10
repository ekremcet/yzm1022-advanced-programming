# Lab Session 2A - Design Patterns

**Course:** YZM1022 - Advanced Programming  
**Date:** 07.04.2026  
**Duration:** 1 hour

---

## Instructions

- This lab consists of **3 questions**, each submitted as a separate Python file.
- You must submit: `q1_factory.py`, `q2_decorator.py`, `q3_observer.py`
- Each file must be **self-contained** and runnable: `python3 q1_factory.py`
- Your code will be tested by running it - make sure the output matches the expected format.
- You may use only the Python standard library (no pip packages).

---

## Grading

| Question  | Topic                  | Points  |
| --------- | ---------------------- | ------- |
| Q1        | Factory Method Pattern | 30      |
| Q2        | Decorator Pattern      | 30      |
| Q3        | Observer Pattern       | 40      |
| **Total** |                        | **100** |

---

## Question 1: Document Factory (30 pts)

**Topics:** Factory Method Pattern

### Task

Build a document creation system using the Factory Method pattern.

### `Document(ABC)` — abstract base:

- Abstract method: `create() -> str`
- Abstract method: `save(filename: str) -> str`
- Abstract property: `extension -> str`

### `PDFDocument`, `WordDocument`, `HTMLDocument` — concrete products:

- Each implements `create()`, `save()`, `extension`
- `save()` returns `"Saved to {filename}.{extension}"`

### `DocumentCreator(ABC)` — abstract creator:

- Abstract factory method: `create_document() -> Document`
- Concrete method: `generate(content: str) -> str` — calls `create_document()` and returns its `create()` result + content

### `PDFCreator`, `WordCreator`, `HTMLCreator` — concrete creators:

- Each overrides `create_document()` to return the matching document type

### Expected Output

```
=== Document Factory ===
PDF: Creating PDF document with content: Annual Report
Word: Creating Word document with content: Meeting Notes
HTML: Creating HTML document with content: Web Page
PDF saved to: report.pdf
Word saved to: notes.docx
HTML saved to: page.html
```

---

## Question 2: Logging Decorators (30 pts)

**Topics:** Decorator Pattern

### Task

Implement a logging system using the Decorator design pattern. Each decorator wraps another logger and adds behavior.

### `Logger(ABC)` — component interface:

- Abstract method: `log(message: str) -> str`

### `ConsoleLogger(Logger)` — concrete component:

- `log()` returns `"[LOG] {message}"`

### `LoggerDecorator(Logger)` — abstract decorator base:

- Stores a wrapped `Logger` instance
- Delegates `log()` to wrapped logger by default

### `TimestampDecorator(LoggerDecorator)`:

- Prepends `"[2026-04-14]"` to message before passing to wrapped logger

### `UpperCaseDecorator(LoggerDecorator)`:

- Converts message to uppercase before passing to wrapped logger

### `PrefixDecorator(LoggerDecorator)`:

- Attribute: `prefix` (str)
- Prepends `"[{prefix}]"` to message before passing to wrapped logger

### Expected Output

```
=== Logging Decorators ===
Simple: [LOG] server started
Timestamp: [LOG] [2026-04-14] server started
Uppercase: [LOG] SERVER STARTED
Prefix: [LOG] [INFO] server started
Combined: [LOG] [2026-04-14] [ERROR] DISK FULL
```

---

## Question 3: Stock Market Observer (40 pts)

**Topics:** Observer Pattern

### Task

Implement a stock market notification system using the Observer pattern.

### `StockObserver(ABC)` — observer interface:

- Abstract method: `update(ticker: str, price: float, change: float)`

### `Investor(StockObserver)`:

- Attributes: `name` (str), `portfolio` (list of tickers)
- `update()` prints: `"  {name}: {ticker} is now ${price:.2f} ({change:+.2f}%)"`
- Only reacts if ticker is in portfolio

### `NewsAgency(StockObserver)`:

- Attribute: `name` (str)
- `update()` always prints: `"  BREAKING: {ticker} moved {change:+.2f}% to ${price:.2f}"`

### `StockMarket` — subject:

- `subscribe(ticker: str, observer: StockObserver)` — per-ticker subscriptions
- `unsubscribe(ticker: str, observer: StockObserver)`
- `update_price(ticker: str, new_price: float)` — computes % change, notifies subscribers of that ticker
- Stores previous prices internally

### Expected Output

```
=== Stock Market Observer ===

AAPL price update: $155.00
  Alice: AAPL is now $155.00 (+3.33%)
  Reuters: BREAKING: AAPL moved +3.33% to $155.00

TSLA price update: $250.00
  Bob: TSLA is now $250.00 (+4.17%)
  Reuters: BREAKING: TSLA moved +4.17% to $250.00

AAPL price update: $148.00
  Alice: AAPL is now $148.00 (-4.52%)
  Reuters: BREAKING: AAPL moved -4.52% to $148.00
```

---

## Submission

Submit a `.zip` file containing:

```
lab-session-2/
├── q1_factory.py
├── q2_decorator.py
└── q3_observer.py
```

Each file must run independently: `python3 qX_filename.py`

**Good luck!**
