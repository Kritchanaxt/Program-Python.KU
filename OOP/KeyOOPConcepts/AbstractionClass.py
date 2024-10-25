
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks, woof, woof")

# Create an object from class Dog
dog = Dog()
dog.sound()