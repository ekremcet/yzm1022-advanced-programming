"""
Lab Session 5 - Question 2: Dynamic Programming - SOLUTION
YZM1022 Advanced Programming
"""


def knapsack(capacity, items):
    """
    0/1 Knapsack with bottom-up dynamic programming.

    Args:
        capacity: maximum total weight the knapsack can hold
        items: list of (weight, value) tuples

    Returns:
        (max_value, dp_table)
        dp_table[i][w] = best value using the first i items with capacity w
    """
    n = len(items)

    # (n + 1) rows, (capacity + 1) columns, all starting at 0
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight, value = items[i - 1]
        for w in range(capacity + 1):
            # Option 1: skip item i-1  -> same value as the row above
            dp[i][w] = dp[i - 1][w]
            # Option 2: take item i-1 (only if it fits) -> keep the better one
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)

    return dp[n][capacity], dp


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
