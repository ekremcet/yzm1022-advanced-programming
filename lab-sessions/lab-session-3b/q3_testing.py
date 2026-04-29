"""
Lab Session 3B — Question 3: Calculator Testing with pytest (40 pts)
See README.md for requirements.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME:
STUDENT ID:
"""

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
# YOUR CODE HERE
# ============================================================
# Write your test functions below.
# Requirements:
#   - Use @pytest.fixture to provide a Calculator instance
#   - Use @pytest.mark.parametrize for at least two tests
#   - Use pytest.raises to test exception cases
#   - Cover all 7 methods with normal, edge, and error cases
#   - At least 15 test cases total
#
# Run with: pytest q3_testing.py -v


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
