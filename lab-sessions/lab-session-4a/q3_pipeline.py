"""
Lab Session 4A — Question 3: Functional Data Pipeline (40 pts)
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME:
STUDENT ID:
"""

from functools import reduce

orders = [
    {"id": 1, "customer": "Alice",   "total": 150.0, "status": "completed", "items": 3},
    {"id": 2, "customer": "Bob",     "total":  80.0, "status": "pending",   "items": 1},
    {"id": 3, "customer": "Charlie", "total": 200.0, "status": "completed", "items": 5},
    {"id": 4, "customer": "Alice",   "total":  50.0, "status": "cancelled", "items": 2},
    {"id": 5, "customer": "Bob",     "total": 120.0, "status": "completed", "items": 4},
    {"id": 6, "customer": "Diana",   "total":  95.0, "status": "pending",   "items": 2},
]

# YOUR CODE HERE
# Assign each answer to the variable name shown:
#   revenue, completed_customers, largest_order, all_pending_small, spending


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
