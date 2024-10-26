
#? Vehicle Management System

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, horsepower, weight):
        self.horsepower = horsepower
        self.weight = weight
        self.mileage = 0

    def fuel_efficiency(self):
        pass

class Car(Vehicle):
    def fuel_efficiency(self):
        return self.horsepower / (self.weight * 0.001)

class Truck(Vehicle):
    def fuel_efficiency(self):
        return (self.horsepower / (self.weight * 0.001)) * 0.8

class Motorcycle(Vehicle):
    def fuel_efficiency(self):
        return (self.horsepower / (self.weight * 0.001)) * 1.2

car = Car(150, 1200)
truck = Truck(300, 4000)
motorcycle = Motorcycle(100, 200)

print("Car fuel efficiency:", car.fuel_efficiency())
print("Truck fuel efficiency:", truck.fuel_efficiency())
print("Motorcycle fuel efficiency:", motorcycle.fuel_efficiency())

