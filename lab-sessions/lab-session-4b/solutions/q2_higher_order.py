"""Lab Session 4B — Q2 Solution: Higher-Order Functions"""


def pipeline(*funcs):
    """Return a function that applies each func left-to-right."""
    def run(value):
        result = value
        for f in funcs:
            result = f(result)
        return result
    return run


def apply_to_all(func, items):
    """Apply func to every item; store None if func raises."""
    results = []
    for item in items:
        try:
            results.append(func(item))
        except Exception:
            results.append(None)
    return results


def group_by(key_func, items):
    """Group items into a dict keyed by key_func(item)."""
    groups = {}
    for item in items:
        key = key_func(item)
        if key not in groups:
            groups[key] = []
        groups[key].append(item)
    return groups


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Higher-Order Functions ===")

    add_tax        = lambda price: round(price * 1.18, 2)
    apply_discount = lambda price: round(price * 0.90, 2)
    to_string      = lambda price: f"${price:.2f}"

    price_display = pipeline(add_tax, apply_discount, to_string)

    print("\npipeline(add_tax, apply_discount, to_string):")
    for p in [100.0, 50.0, 200.0]:
        print(f"  {p} → {price_display(p)}")

    def safe_sqrt(x):
        if x < 0:
            raise ValueError("negative input")
        return x ** 0.5

    values = [4, 9, -1, 16, -4, 25]
    results = apply_to_all(safe_sqrt, values)

    print("\napply_to_all(safe_sqrt, [4, 9, -1, 16, -4, 25]):")
    print(f"  {results}")

    words = ["apple", "banana", "cherry", "avocado", "blueberry", "citrus"]
    grouped = group_by(lambda w: w[0], words)

    print("\ngroup_by(first letter, words):")
    for letter in sorted(grouped):
        print(f"  '{letter}': {grouped[letter]}")
