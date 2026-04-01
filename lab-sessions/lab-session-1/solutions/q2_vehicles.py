"""
Lab Session 1 — Question 2: Vehicle Fleet System
Topics: Inheritance, Polymorphism, ABC, Method Overriding (Week 2-3)
"""
from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = 0.0

    @property
    def mileage(self) -> float:
        return self._mileage

    @property
    @abstractmethod
    def vehicle_type(self) -> str:
        pass

    @abstractmethod
    def fuel_cost(self, distance: float) -> float:
        pass

    def drive(self, distance: float):
        self._mileage += distance
        print(f"  {self.vehicle_type} drove {distance} km")

    def __str__(self) -> str:
        return f"  {self.year} {self.brand} {self.model} ({self.vehicle_type}) - {self._mileage:.0f} km"


class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, fuel_efficiency: float = 15.0):
        super().__init__(brand, model, year)
        self.fuel_efficiency = fuel_efficiency  # km per liter

    @property
    def vehicle_type(self) -> str:
        return "Car"

    def fuel_cost(self, distance: float) -> float:
        return distance / self.fuel_efficiency * 7.5  # 7.5 per liter


class ElectricCar(Car):
    def __init__(self, brand: str, model: str, year: int):
        super().__init__(brand, model, year, fuel_efficiency=0)

    @property
    def vehicle_type(self) -> str:
        return "Electric Car"

    def fuel_cost(self, distance: float) -> float:
        return distance * 0.15 * 3.0  # 0.15 kWh/km * 3.0 per kWh


class Truck(Vehicle):
    def __init__(self, brand: str, model: str, year: int, cargo_capacity: float = 10.0):
        super().__init__(brand, model, year)
        self.cargo_capacity = cargo_capacity  # tons

    @property
    def vehicle_type(self) -> str:
        return "Truck"

    def fuel_cost(self, distance: float) -> float:
        return distance / 5.0 * 7.5  # 5 km/L for trucks

    def load(self, weight: float):
        if weight > self.cargo_capacity:
            raise ValueError(f"Weight {weight}t exceeds capacity {self.cargo_capacity}t")
        print(f"  Loaded {weight}t onto {self.brand} {self.model}")


class Fleet:
    def __init__(self):
        self._vehicles: list = []

    def add_vehicle(self, vehicle: Vehicle):
        if not isinstance(vehicle, Vehicle):
            raise TypeError("Only Vehicle instances can be added to the fleet")
        self._vehicles.append(vehicle)

    def total_fuel_cost(self, distance: float) -> float:
        return sum(v.fuel_cost(distance) for v in self._vehicles)

    def get_by_type(self, vehicle_type: str) -> list:
        return [v for v in self._vehicles if v.vehicle_type == vehicle_type]

    def __len__(self) -> int:
        return len(self._vehicles)

    def __iter__(self):
        return iter(self._vehicles)


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

    print(f"\nCars in fleet: {len(fleet.get_by_type('Car')) + len(fleet.get_by_type('Electric Car'))}")
    print(f"Trucks in fleet: {len(fleet.get_by_type('Truck'))}")
