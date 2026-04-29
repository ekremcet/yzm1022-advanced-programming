"""
Lab Session 3A — Question 3: Unit Testing with pytest (40 pts)
See README.md for requirements.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME:
STUDENT ID:
"""

import pytest


# ============================================================
# PROVIDED CLASS — do not modify
# ============================================================
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

    def transfer(self, other: "BankAccount", amount: float):
        self.withdraw(amount)
        other.deposit(amount)


# ============================================================
# YOUR CODE HERE
# ============================================================
# Write your test functions below.
# Requirements:
#   - Use @pytest.fixture to create a funded account (balance=1000) and an empty account
#   - Use @pytest.mark.parametrize for at least one test (e.g. multiple deposit amounts)
#   - Use pytest.raises to test exception cases
#   - Cover: init, deposit, withdraw, transfer, sequential operations
#   - At least 15 test cases total
#
# Run with: pytest q3_testing.py -v


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    import subprocess
    import sys

    print("=== Running BankAccount Tests ===\n")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", __file__, "-v", "--tb=short"],
        capture_output=False,
    )
    if result.returncode == 0:
        print("\n=== All tests passed! ===")
    else:
        print("\n=== SOME TESTS FAILED ===")
        sys.exit(1)
