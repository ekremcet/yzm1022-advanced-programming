"""
Lab Session 1 — Question 3: Restaurant Order System
Topics: Composition, Interfaces (ABC), Dependency Injection (Week 3)
"""
from abc import ABC, abstractmethod


class MenuItem:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category  # "food", "drink", "dessert"

    def __str__(self) -> str:
        return f"{self.name} (${self.price:.2f})"


class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> str:
        pass

    @property
    @abstractmethod
    def method_name(self) -> str:
        pass


class CreditCardPayment(PaymentMethod):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def process_payment(self, amount: float) -> str:
        return f"Charged ${amount:.2f} to card ending {self.card_number[-4:]}"

    @property
    def method_name(self) -> str:
        return "Credit Card"


class CashPayment(PaymentMethod):
    def process_payment(self, amount: float) -> str:
        return f"Received ${amount:.2f} in cash"

    @property
    def method_name(self) -> str:
        return "Cash"


class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, total: float) -> float:
        return total * (1 - self.percentage / 100)

    @property
    def description(self) -> str:
        return f"{self.percentage:.0f}% off"


class FixedDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, total: float) -> float:
        return max(0, total - self.amount)

    @property
    def description(self) -> str:
        return f"${self.amount:.2f} off"


class Order:
    def __init__(self, table_number: int, payment: PaymentMethod,
                 discount: DiscountStrategy = None):
        self.table_number = table_number
        self.payment = payment  # Composition + DI
        self.discount = discount  # Composition + DI
        self._items: list = []

    def add_item(self, item: MenuItem):
        self._items.append(item)

    def remove_item(self, item_name: str):
        self._items = [i for i in self._items if i.name != item_name]

    @property
    def subtotal(self) -> float:
        return sum(item.price for item in self._items)

    @property
    def total(self) -> float:
        if self.discount:
            return self.discount.apply_discount(self.subtotal)
        return self.subtotal

    def checkout(self) -> str:
        return self.payment.process_payment(self.total)

    def __str__(self) -> str:
        lines = [f"--- Order for Table {self.table_number} ---"]
        lines.append("Items:")
        for i, item in enumerate(self._items, 1):
            lines.append(f"  {i}. {item}")
        lines.append(f"Subtotal: ${self.subtotal:.2f}")
        if self.discount:
            lines.append(f"Discount: {self.discount.description}")
        lines.append(f"Total: ${self.total:.2f}")
        lines.append(f"Payment: {self.payment.method_name}")
        return "\n".join(lines)


if __name__ == "__main__":
    print("=== Restaurant Order System ===")

    # Menu items
    burger = MenuItem("Burger", 12.99, "food")
    fries = MenuItem("Fries", 4.99, "food")
    cola = MenuItem("Cola", 2.50, "drink")
    cheesecake = MenuItem("Cheesecake", 7.99, "dessert")
    pizza = MenuItem("Pizza", 15.99, "food")
    water = MenuItem("Water", 1.50, "drink")

    # Order 1: Credit card + percentage discount
    order1 = Order(
        table_number=5,
        payment=CreditCardPayment("4111111111114242"),
        discount=PercentageDiscount(10)
    )
    order1.add_item(burger)
    order1.add_item(fries)
    order1.add_item(cola)
    order1.add_item(cheesecake)

    print(f"\n{order1}")
    print(f"\nProcessing payment...")
    print(order1.checkout())

    # Order 2: Cash + fixed discount
    order2 = Order(
        table_number=3,
        payment=CashPayment(),
        discount=FixedDiscount(5.00)
    )
    order2.add_item(pizza)
    order2.add_item(water)

    print(f"\n{order2}")
    print(f"\nProcessing payment...")
    print(order2.checkout())
