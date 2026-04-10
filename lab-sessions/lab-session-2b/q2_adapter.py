"""
Lab Session 2B — Question 2: Payment Adapter
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
    print("=== Payment Adapter ===")

    # Legacy system
    legacy_system = LegacyPaymentSystem()

    # Alice with account 12345
    alice_adapter = PaymentAdapter(legacy_system, "12345")
    alice_store = OnlineStore(alice_adapter)

    print(f"\nAlice's initial balance: ${alice_adapter.get_balance():.2f}")
    print(f"\nBuying laptop for $800.00...")
    result = alice_store.buy("laptop", 800.00)
    print(f"{result}")
    print(f"\nAlice's remaining balance: ${alice_adapter.get_balance():.2f}")

    # Bob with account 67890
    bob_adapter = PaymentAdapter(legacy_system, "67890")
    bob_store = OnlineStore(bob_adapter)

    print(f"\nBob's initial balance: ${bob_adapter.get_balance():.2f}")
    print(f"\nBuying expensive watch for $600.00...")
    result = bob_store.buy("expensive watch", 600.00)
    print(f"{result}")
    print(f"\nBob's remaining balance: ${bob_adapter.get_balance():.2f}")