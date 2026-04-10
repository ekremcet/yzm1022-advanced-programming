"""
Lab Session 2B — Question 1: Pizza Order Builder
See README.md for requirements. Do NOT modify the test code below.

FILL OUT THE FOLLOWING INFORMATION
STUDENT NAME: Solution
STUDENT ID: 000000
"""


class Pizza:
    def __init__(self, size, crust, sauce, toppings, extra_cheese):
        self.size = size
        self.crust = crust
        self.sauce = sauce
        self.toppings = toppings
        self.extra_cheese = extra_cheese
    
    def __str__(self):
        lines = [f"{self.size} {self.crust} pizza with {self.sauce} sauce"]
        if self.toppings:
            lines.append(f"Toppings: {', '.join(self.toppings)}")
        lines.append(f"Extra cheese: {'Yes' if self.extra_cheese else 'No'}")
        return "\n".join(lines)


class PizzaBuilder:
    def __init__(self):
        self.size = None
        self.crust = None
        self.sauce = None
        self.toppings = []
        self.extra_cheese_flag = False
    
    def set_size(self, size):
        self.size = size
        return self
    
    def set_crust(self, crust):
        self.crust = crust
        return self
    
    def set_sauce(self, sauce):
        self.sauce = sauce
        return self
    
    def add_topping(self, topping):
        self.toppings.append(topping)
        return self
    
    def extra_cheese(self):
        self.extra_cheese_flag = True
        return self
    
    def build(self):
        if self.size is None:
            raise ValueError("Size must be set before building pizza")
        return Pizza(self.size, self.crust, self.sauce, self.toppings.copy(), self.extra_cheese_flag)


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