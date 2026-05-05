"""Lab Session 3B — Q3 Solution: Calculator Testing with pytest"""

import pytest


# ============================================================
# PROVIDED CLASS — do not modify
# ============================================================
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


# ============================================================
# FIXTURE
# ============================================================
@pytest.fixture
def calc():
    return Calculator()


# ============================================================
# ADD
# ============================================================
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-2, 3, 1),
    (-2, -3, -5),
    (0, 0, 0),
    (0, 5, 5),
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


# ============================================================
# SUBTRACT
# ============================================================
def test_subtract_normal(calc):
    assert calc.subtract(5, 3) == 2


def test_subtract_negative_result(calc):
    assert calc.subtract(3, 5) == -2


# ============================================================
# MULTIPLY
# ============================================================
@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (-2, 3, -6),
    (5, 0, 0),
    (7, 1, 7),
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


# ============================================================
# DIVIDE
# ============================================================
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5.0),
    (7, 2, 3.5),
    (-6, 3, -2.0),
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == pytest.approx(expected)


def test_divide_by_zero_raises(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.divide(5, 0)


# ============================================================
# POWER
# ============================================================
def test_power_normal(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 2) == 25


def test_power_edge_cases(calc):
    assert calc.power(5, 0) == 1   # anything^0 == 1
    assert calc.power(0, 5) == 0   # 0^anything == 0


def test_power_negative_exponent_raises(calc):
    with pytest.raises(ValueError, match="Exponent cannot be negative"):
        calc.power(2, -1)


# ============================================================
# SQRT
# ============================================================
def test_sqrt_normal(calc):
    assert calc.sqrt(4) == pytest.approx(2.0)
    assert calc.sqrt(9) == pytest.approx(3.0)
    assert calc.sqrt(2) == pytest.approx(1.4142135, rel=1e-5)


def test_sqrt_negative_raises(calc):
    with pytest.raises(ValueError, match="Cannot take square root of negative number"):
        calc.sqrt(-1)


# ============================================================
# FACTORIAL
# ============================================================
def test_factorial_normal(calc):
    assert calc.factorial(5) == 120
    assert calc.factorial(3) == 6


def test_factorial_edge_cases(calc):
    assert calc.factorial(0) == 1
    assert calc.factorial(1) == 1


def test_factorial_negative_raises(calc):
    with pytest.raises(ValueError, match="Cannot calculate factorial of negative number"):
        calc.factorial(-1)


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    import subprocess
    import sys

    print("=== Running Calculator Tests ===\n")
    result = subprocess.run(
        [sys.executable, "-m", "pytest", __file__, "-v", "--tb=short"],
        capture_output=False,
    )
    if result.returncode == 0:
        print("\n=== All tests passed! ===")
    else:
        print("\n=== SOME TESTS FAILED ===")
        sys.exit(1)
