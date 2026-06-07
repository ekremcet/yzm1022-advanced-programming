"""Lab Session 4A — Q2 Solution: Immutable Data Transformations"""


def apply_discount(product: dict, percent: float) -> dict:
    """Return a NEW dict with price reduced by percent%. Original unchanged."""
    return {**product, "price": round(product["price"] * (1 - percent / 100), 2)}


def mark_out_of_stock(product: dict) -> dict:
    """Return a NEW dict with in_stock set to False. Original unchanged."""
    return {**product, "in_stock": False}


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    products = [
        {"id": 1, "name": "Laptop",     "price": 1200.0, "category": "Electronics", "in_stock": True},
        {"id": 2, "name": "Book",       "price":   15.0, "category": "Education",   "in_stock": True},
        {"id": 3, "name": "Headphones", "price":   80.0, "category": "Electronics", "in_stock": False},
        {"id": 4, "name": "Notebook",   "price":    5.0, "category": "Education",   "in_stock": True},
        {"id": 5, "name": "Webcam",     "price":   60.0, "category": "Electronics", "in_stock": True},
    ]

    print("=== Immutable Data Transformations ===")

    # apply_discount
    discounted = apply_discount(products[0], 10)
    print(f"\napply_discount(Laptop, 10%):")
    print(f"  New price:       ${discounted['price']:.2f}")
    print(f"  Original price:  ${products[0]['price']:.2f}  (must be unchanged)")

    # mark_out_of_stock
    out = mark_out_of_stock(products[1])
    print(f"\nmark_out_of_stock(Book):")
    print(f"  New in_stock:      {out['in_stock']}")
    print(f"  Original in_stock: {products[1]['in_stock']}   (must be unchanged)")

    # List comprehension: in-stock Electronics with 15% discount
    discounted_electronics = [
        apply_discount(p, 15)
        for p in products
        if p["category"] == "Electronics" and p["in_stock"]
    ]
    print(f"\nIn-stock Electronics after 15% discount:")
    for p in discounted_electronics:
        print(f"  {p['name']}: ${p['price']:.2f}")
    print(f"\nOriginal prices unchanged:")
    for p in products:
        print(f"  {p['name']}: ${p['price']:.2f}")
