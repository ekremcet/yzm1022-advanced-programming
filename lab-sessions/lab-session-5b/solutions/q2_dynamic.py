"""
Lab Session 5B - Question 2: Dynamic Programming Algorithms - SOLUTION
YZM1022 Advanced Programming
"""


def lcs_length(s1, s2):
    """Length of the Longest Common Subsequence using bottom-up DP.
    Build the DP table, print it, and return the LCS length."""
    m, n = len(s1), len(s2)

    # dp[i][j] = LCS length of s1[:i] and s2[:j]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Print the DP table with row/column labels
    print("DP Table:")
    print('     ""  ' + "  ".join(s2))
    for i in range(m + 1):
        label = '""' if i == 0 else s1[i - 1]
        print(f"{label:<3}" + "  ".join(f"{dp[i][j]:2}" for j in range(n + 1)))

    return dp[m][n]


def min_coins(coins, amount):
    """Minimum number of coins needed to make `amount`, or -1 if impossible.
    Use a bottom-up DP array."""
    # dp[a] = fewest coins needed to make amount a; start "impossible" everywhere
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                dp[a] = min(dp[a], dp[a - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


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
