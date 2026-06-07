"""
Lab Session 5 - Question 2: Dynamic Programming (30 pts)
See README.md for the full description.

Implement the function marked `# YOUR CODE HERE`.
Do NOT modify the test block at the bottom - it prints the expected output.
"""


def knapsack(capacity, items):
    """
    0/1 Knapsack with bottom-up dynamic programming.

    items: a list of (weight, value) tuples.
    Build a table where dp_table[i][w] = the best total value using the first i
    items with a knapsack of capacity w. The table has len(items) + 1 rows and
    capacity + 1 columns, all starting at 0.

    Returns (max_value, dp_table).
    """
    # YOUR CODE HERE
    pass


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== 0/1 Knapsack (Dynamic Programming) ===")

    items = [(2, 3), (3, 4), (4, 5), (5, 6)]  # (weight, value)
    capacity = 5

    print(f"Items (weight, value): {items}")
    print(f"Capacity: {capacity}\n")

    max_value, dp_table = knapsack(capacity, items)

    print("DP table (rows = first i items, cols = capacity 0..C):")
    for row in dp_table:
        print("  " + " ".join(f"{v:4}" for v in row))

    print(f"\nMaximum value: {max_value}")
