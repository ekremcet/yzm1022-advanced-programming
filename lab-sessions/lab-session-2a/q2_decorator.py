"""
Lab Session 2 — Question 2: Logging Decorators (30 pts)
See README.md for requirements. Do NOT modify the test code below.
"""


# YOUR CODE HERE


# ============================================================
# DO NOT MODIFY THE CODE BELOW
# ============================================================
if __name__ == "__main__":
    print("=== Logging Decorators ===")

    base = ConsoleLogger()
    ts = TimestampDecorator(ConsoleLogger())
    upper = UpperCaseDecorator(ConsoleLogger())
    prefix = PrefixDecorator(ConsoleLogger(), "INFO")
    combined = UpperCaseDecorator(TimestampDecorator(PrefixDecorator(ConsoleLogger(), "ERROR")))

    print(f"Simple: {base.log('server started')}")
    print(f"Timestamp: {ts.log('server started')}")
    print(f"Uppercase: {upper.log('server started')}")
    print(f"Prefix: {prefix.log('server started')}")
    print(f"Combined: {combined.log('disk full')}")
