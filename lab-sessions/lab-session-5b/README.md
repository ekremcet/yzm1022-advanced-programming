# Lab Session 5B: Recursion/DP/Generics

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

| Question  | Topic                                  | Points  |
| --------- | -------------------------------------- | ------- |
| Q1        | Recursive Algorithms, Problem Solving  | 30      |
| Q2        | Dynamic Programming, String Algorithms | 30      |
| Q3        | Generic Data Structures, Type Safety   | 40      |
| **Total** |                                        | **100** |

---

## Question 1: Tower of Hanoi (30 pts)

**Topics:** Recursion, Divide and Conquer

Implement one recursive function.

### `tower_of_hanoi(n, src, dst, aux)`:

- Solve the classic Tower of Hanoi puzzle for `n` disks.
- Move all disks from the source peg `src` to the destination peg `dst`, using `aux` as
  the spare peg, never placing a larger disk on a smaller one.
- Print each move as `"Move disk from {src} to {dst}"`.
- Return the total number of moves made (it should be `2**n - 1`).
- **Idea:** to move `n` disks from `src` to `dst`, first move the top `n-1` disks to
  `aux`, then move the largest disk to `dst`, then move the `n-1` disks from `aux` to `dst`.

### Expected Output

```
=== Tower of Hanoi ===

Moves for 3 disks:
Move disk from A to C
Move disk from A to B
Move disk from C to B
Move disk from A to C
Move disk from B to A
Move disk from B to C
Move disk from A to C
Total moves: 7
```

---

## Question 2: Dynamic Programming Algorithms (30 pts)

**Topics:** Dynamic Programming, String Algorithms, Optimization

Implement two classic DP problems.

### `lcs_length(s1, s2)`:

- Compute the **length** of the Longest Common Subsequence using **bottom-up DP**.
- Build and print the full DP table.
- Return the length.
- _(You only need the length - you do not have to reconstruct the actual subsequence.)_

### `min_coins(coins, amount)`:

- Find the minimum number of coins needed to make `amount`.
- Return `-1` if it is impossible.
- Use a **bottom-up DP** array where `dp[a]` is the fewest coins to make amount `a`.

### Expected Output

```
=== Dynamic Programming Algorithms ===

Longest Common Subsequence:
String 1: "ABCDGH"
String 2: "AEDFHR"

DP Table:
     ""  A  E  D  F  H  R
""  0   0   0   0   0   0   0
A   0   1   1   1   1   1   1
B   0   1   1   1   1   1   1
C   0   1   1   1   1   1   1
D   0   1   1   2   2   2   2
G   0   1   1   2   2   2   2
H   0   1   1   2   2   3   3

LCS length: 3

Coin Change Problem:
Coins: [1, 3, 4]
Amount: 6 → Minimum coins: 2
Amount: 8 → Minimum coins: 2
Amount: 11 → Minimum coins: 3
Amount: 2 → Minimum coins: 2
```

---

## Question 3: Generic Data Structures (40 pts)

**Topics:** Generic Programming, Type Annotations, Data Structures

Implement a generic `Stack[T]`, a small `Point` class, and a bracket checker.

### `Stack[T]` class:

Generic stack that works with any type `T`.

- `push(item: T) -> None`: add item to the top
- `pop() -> T`: remove and return the top item (raise `IndexError` if empty)
- `peek() -> T`: return the top item without removing it (raise `IndexError` if empty)
- `is_empty() -> bool`
- `__len__() -> int`
- `__iter__()`: iterate from top to bottom

### `Point` class (for demonstrating the stack with a custom type):

```python
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point({self.x}, {self.y})"
```

### `is_balanced(expression)`:

- Use your `Stack` to check whether the brackets in `expression` are balanced.
- Support `()`, `[]`, `{}`. Return `True` if balanced, `False` otherwise.

### Expected Output

```
=== Generic Data Structures ===

Testing Stack with integers:
Stack contents (top to bottom): [30, 20, 10]
Popped: 30
Popped: 20
Stack size: 1

Testing with custom Point class:
Point stack: ['Point(3.0, 4.0)', 'Point(1.0, 2.0)']

Bracket Balance Checker:
"((()))" → True
"([{}])" → True
"([)]" → False
"" → True
"(((" → False
```

---

## Submission

Submit a `.zip` file containing:

```
lab-session-5b/
├── q1_recursion.py
├── q2_dynamic.py
└── q3_generics.py
```

Each file must run independently: `python3 qX_filename.py`

**Good luck!**
