"""
Lab Session 2B — Question 2: Payment Adapter
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME: Solution
STUDENT ID: 000000
"""

from abc import ABC, abstractmethod


class LegacyPaymentSystem:
    def __init__(self):
        self.account_balance = {"12345": 1000.0, "67890": 500.0}
    
    def make_payment(self, amount, account):
        return f"Payment of ${amount} charged to account {account}"
    
    def check_balance(self, account):
        return self.account_balance.get(account, 0.0)


class ModernPaymentAPI(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    
    @abstractmethod
    def get_balance(self):
        pass


class PaymentAdapter(ModernPaymentAPI):
    def __init__(self, legacy_system, account):
        self.legacy_system = legacy_system
        self.account = account
    
    def pay(self, amount):
        result = self.legacy_system.make_payment(amount, self.account)
        print(result)
        return True
    
    def get_balance(self):
        return self.legacy_system.check_balance(self.account)


class OnlineStore:
    def __init__(self, payment_api):
        self.payment_api = payment_api
    
    def buy(self, item, price):
        balance = self.payment_api.get_balance()
        if balance >= price:
            if self.payment_api.pay(price):
                return f"Purchase successful: {item}"
        else:
            return f"Insufficient funds for {item} (need ${price:.2f}, have ${balance:.2f})"
        return f"Payment failed for {item}"


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