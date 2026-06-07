"""
Lab Session 4A — Question 1: Pure Functions (30 pts)
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME:
STUDENT ID:
"""

import datetime

# YOUR CODE HERE


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Pure Functions ===")

    print("\n--- 1a: Price Calculator ---")
    print(f"$100.00 with 20% discount: ${calculate_price_pure(100.0, 0.20):.2f}")
    print(f"$50.00  with 10% discount: ${calculate_price_pure(50.0,  0.10):.2f}")

    print("\n--- 1b: Tag Normalizer ---")
    original = ["  Python  ", "JAVA", "  rust"]
    result   = normalize_tags_pure(original)
    print(f"Output:             {result}")
    print(f"Original unchanged: {original}")

    print("\n--- 1c: Age Category ---")
    print(f"Born 2010, year 2024: {get_age_category_pure(2010, 2024)}")
    print(f"Born 2000, year 2024: {get_age_category_pure(2000, 2024)}")
    print(f"Born 1950, year 2024: {get_age_category_pure(1950, 2024)}")
