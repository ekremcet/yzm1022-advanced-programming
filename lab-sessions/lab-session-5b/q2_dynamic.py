"""
Lab Session 5B - Question 2: Dynamic Programming Algorithms (30 pts)
See README.md for the full description.

Implement each function marked `# YOUR CODE HERE`.
Do NOT modify the test block at the bottom - it prints the expected output.
"""


def lcs_length(s1, s2):
    """Length of the Longest Common Subsequence using bottom-up DP.
    Build the DP table, print it, and return the LCS length."""
    # YOUR CODE HERE
    pass


def min_coins(coins, amount):
    """Minimum number of coins needed to make `amount`, or -1 if impossible.
    Use a bottom-up DP array."""
    # YOUR CODE HERE
    pass


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Dynamic Programming Algorithms ===")

    print("\nLongest Common Subsequence:")
    s1, s2 = "ABCDGH", "AEDFHR"
    print(f'String 1: "{s1}"')
    print(f'String 2: "{s2}"')
    print()
    length = lcs_length(s1, s2)
    print(f"\nLCS length: {length}")

    print("\nCoin Change Problem:")
    coins = [1, 3, 4]
    print(f"Coins: {coins}")
    for amount in [6, 8, 11, 2]:
        result = min_coins(coins, amount)
        if result == -1:
            print(f"Amount: {amount} → Impossible")
        else:
            print(f"Amount: {amount} → Minimum coins: {result}")
