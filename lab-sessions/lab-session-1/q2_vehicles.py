"""
Lab Session 1 — Question 2: Vehicle Fleet System
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
    print("=== Vehicle Fleet System ===")

    fleet = Fleet()
    car = Car("Toyota", "Corolla", 2024, fuel_efficiency=15.0)
    ecar = ElectricCar("Tesla", "Model3", 2024)
    truck1 = Truck("Volvo", "FH16", 2024, cargo_capacity=20.0)
    truck2 = Truck("Ford", "Transit", 2023, cargo_capacity=5.0)

    fleet.add_vehicle(car)
    fleet.add_vehicle(ecar)
    fleet.add_vehicle(truck1)
    fleet.add_vehicle(truck2)

    print(f"Fleet size: {len(fleet)}")

    print("\nAll vehicles:")
    for v in fleet:
        print(v)

    print("\nDriving all vehicles 100 km...")
    for v in fleet:
        v.drive(100)

    print("\nFuel costs for 500 km trip:")
    for v in fleet:
        cost = v.fuel_cost(500)
        print(f"  {v.brand} {v.model}: ${cost:.2f}")
    print(f"  Total fleet cost: ${fleet.total_fuel_cost(500):.2f}")

    cars = fleet.get_by_type("Car") + fleet.get_by_type("Electric Car")
    trucks = fleet.get_by_type("Truck")
    print(f"\nCars in fleet: {len(cars)}")
    print(f"Trucks in fleet: {len(trucks)}")
