"""
Lab Session 2 — Question 3: Stock Market Observer (40 pts)
See README.md for requirements. Do NOT modify the test code below.
"""


# YOUR CODE HERE


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Stock Market Observer ===")

    market = StockMarket()
    market.set_price("AAPL", 150.0)
    market.set_price("TSLA", 240.0)

    alice = Investor("Alice", ["AAPL", "MSFT"])
    bob = Investor("Bob", ["TSLA", "AAPL"])
    reuters = NewsAgency("Reuters")

    market.subscribe("AAPL", alice)
    market.subscribe("AAPL", reuters)
    market.subscribe("TSLA", bob)
    market.subscribe("TSLA", reuters)

    print("\nAAPL price update: $155.00")
    market.update_price("AAPL", 155.0)

    print("\nTSLA price update: $250.00")
    market.update_price("TSLA", 250.0)

    print("\nAAPL price update: $148.00")
    market.update_price("AAPL", 148.0)
