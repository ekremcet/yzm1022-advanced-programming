"""
Lab Session 4A — Question 2: Immutable Data Transformations (30 pts)
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME:
STUDENT ID:
"""

# YOUR CODE HERE


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

    discounted = apply_discount(products[0], 10)
    print(f"\napply_discount(Laptop, 10%):")
    print(f"  New price:       ${discounted['price']:.2f}")
    print(f"  Original price:  ${products[0]['price']:.2f}  (must be unchanged)")

    out = mark_out_of_stock(products[1])
    print(f"\nmark_out_of_stock(Book):")
    print(f"  New in_stock:      {out['in_stock']}")
    print(f"  Original in_stock: {products[1]['in_stock']}   (must be unchanged)")

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
