"""Lab Session 4A — Q3 Solution: Functional Data Pipeline"""

from functools import reduce

orders = [
    {"id": 1, "customer": "Alice",   "total": 150.0, "status": "completed", "items": 3},
    {"id": 2, "customer": "Bob",     "total":  80.0, "status": "pending",   "items": 1},
    {"id": 3, "customer": "Charlie", "total": 200.0, "status": "completed", "items": 5},
    {"id": 4, "customer": "Alice",   "total":  50.0, "status": "cancelled", "items": 2},
    {"id": 5, "customer": "Bob",     "total": 120.0, "status": "completed", "items": 4},
    {"id": 6, "customer": "Diana",   "total":  95.0, "status": "pending",   "items": 2},
]


revenue = sum(o["total"] * 0.95 for o in orders if o["status"] == "completed")

completed_customers = sorted(set(o["customer"] for o in orders if o["status"] == "completed"))

largest_order = max(orders, key=lambda o: o["items"])

all_pending_small = all(o["total"] < 100 for o in orders if o["status"] == "pending")

spending = {
    customer: sum(o["total"] for o in orders if o["customer"] == customer)
    for customer in set(o["customer"] for o in orders)
}


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Functional Data Pipeline ===")
    print(f"\nRevenue (completed, 5% discount): ${revenue:.2f}")
    print(f"Completed customers:              {completed_customers}")
    print(f"Largest order:                    id={largest_order['id']}, customer={largest_order['customer']}")
    print(f"All pending orders under $100:    {all_pending_small}")
    print(f"\nTotal spend per customer:")
    for customer, total in sorted(spending.items()):
        print(f"  {customer}: ${total:.2f}")
