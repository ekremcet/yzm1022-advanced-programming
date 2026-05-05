"""Lab Session 3A — Q3 Solution: Unit Testing with pytest"""

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
# FIXTURES
# ============================================================
@pytest.fixture
def account():
    """A funded account with balance=1000."""
    return BankAccount("Alice", 1000)


@pytest.fixture
def empty_account():
    """An account with default zero balance."""
    return BankAccount("Bob")


# ============================================================
# INIT TESTS
# ============================================================
def test_initial_balance(account):
    assert account.balance == 1000


def test_default_zero_balance(empty_account):
    assert empty_account.balance == 0


def test_negative_initial_raises():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount("Eve", -100)


# ============================================================
# DEPOSIT TESTS
# ============================================================
@pytest.mark.parametrize("amount, expected_balance", [
    (500,  1500),
    (100,  1100),
    (0.01, 1000.01),
])
def test_deposit(account, amount, expected_balance):
    account.deposit(amount)
    assert account.balance == pytest.approx(expected_balance)


def test_deposit_returns_new_balance(account):
    result = account.deposit(200)
    assert result == 1200


@pytest.mark.parametrize("invalid_amount", [0, -50, -0.01])
def test_deposit_invalid_raises(account, invalid_amount):
    with pytest.raises(ValueError, match="Deposit must be positive"):
        account.deposit(invalid_amount)


# ============================================================
# WITHDRAW TESTS
# ============================================================
def test_withdraw_valid(account):
    account.withdraw(300)
    assert account.balance == 700


def test_withdraw_returns_new_balance(account):
    result = account.withdraw(400)
    assert result == 600


def test_withdraw_all_funds(account):
    account.withdraw(1000)
    assert account.balance == 0


def test_withdraw_insufficient_raises(account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(2000)


@pytest.mark.parametrize("invalid_amount", [0, -10])
def test_withdraw_invalid_raises(account, invalid_amount):
    with pytest.raises(ValueError, match="Withdrawal must be positive"):
        account.withdraw(invalid_amount)


# ============================================================
# TRANSFER TESTS
# ============================================================
def test_transfer_updates_both_balances(account, empty_account):
    account.transfer(empty_account, 300)
    assert account.balance == 700
    assert empty_account.balance == 300


def test_transfer_insufficient_raises(account, empty_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.transfer(empty_account, 5000)


# ============================================================
# SEQUENTIAL OPERATIONS
# ============================================================
def test_multiple_sequential_operations(account):
    account.deposit(500)    # 1500
    account.withdraw(200)   # 1300
    account.deposit(100)    # 1400
    account.withdraw(400)   # 1000
    assert account.balance == 1000


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
