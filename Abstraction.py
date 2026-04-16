# 5_abstraction.py
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    @abstractmethod
    def fuel_type(self):
        pass

    def display(self):
        print(f"{self.name} - Speed: {self.speed}km/h - Fuel: {self.fuel_type()}")

class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric ⚡"

class PetrolCar(Vehicle):
    def fuel_type(self):
        return "Petrol ⛽"

class Bicycle(Vehicle):
    def fuel_type(self):
        return "No Fuel 🚲"

# Test
vehicles = [
    ElectricCar("Tesla", 250),
    PetrolCar("BMW", 220),
    Bicycle("Trek", 30)
]

for v in vehicles:
    v.display()