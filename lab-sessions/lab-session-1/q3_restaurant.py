"""
Lab Session 1 — Question 3: Restaurant Order System
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
    print("=== Restaurant Order System ===")

    burger = MenuItem("Burger", 12.99, "food")
    fries = MenuItem("Fries", 4.99, "food")
    cola = MenuItem("Cola", 2.50, "drink")
    cheesecake = MenuItem("Cheesecake", 7.99, "dessert")
    pizza = MenuItem("Pizza", 15.99, "food")
    water = MenuItem("Water", 1.50, "drink")

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
