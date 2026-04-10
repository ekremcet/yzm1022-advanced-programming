"""
Lab Session 2B — Question 1: Pizza Order Builder
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
    print("=== Pizza Order Builder ===")
    print("\nBuilding pizzas using builder pattern...")

    # Pizza 1: Large pepperoni with mushrooms
    builder1 = PizzaBuilder()
    pizza1 = (builder1
              .set_size("Large")
              .set_crust("Thin Crust")
              .set_sauce("Marinara")
              .add_topping("Pepperoni")
              .add_topping("Mushrooms")
              .extra_cheese()
              .build())

    print(f"\nPizza 1: {pizza1}")

    # Pizza 2: Medium BBQ chicken
    builder2 = PizzaBuilder()
    pizza2 = (builder2
              .set_size("Medium")
              .set_crust("Thick Crust")
              .set_sauce("BBQ")
              .add_topping("Chicken")
              .add_topping("Onions")
              .add_topping("Bell peppers")
              .build())

    print(f"\nPizza 2: {pizza2}")

    # Pizza 3: Small spinach white sauce
    builder3 = PizzaBuilder()
    pizza3 = (builder3
              .set_size("Small")
              .set_crust("Hand-tossed")
              .set_sauce("White")
              .add_topping("Spinach")
              .extra_cheese()
              .build())

    print(f"\nPizza 3: {pizza3}")