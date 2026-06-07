"""Lab Session 4A — Q1 Solution: Pure Functions"""

import datetime


# --- 1a ---
DISCOUNT = 0.20

def calculate_price(original_price):
    return original_price * (1 - DISCOUNT)

def calculate_price_pure(original_price: float, discount: float) -> float:
    return original_price * (1 - discount)


# --- 1b ---
def normalize_tags(tags):
    for i in range(len(tags)):
        tags[i] = tags[i].lower().strip()
    return tags

def normalize_tags_pure(tags: list) -> list:
    return [tag.lower().strip() for tag in tags]


# --- 1c ---
def get_age_category(birth_year):
    age = datetime.datetime.now().year - birth_year
    if age < 18:   return "minor"
    if age < 65:   return "adult"
    return "senior"

def get_age_category_pure(birth_year: int, current_year: int) -> str:
    age = current_year - birth_year
    if age < 18:   return "minor"
    if age < 65:   return "adult"
    return "senior"


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
