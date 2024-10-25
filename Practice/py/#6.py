
#? AbstractionClass

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks, woof, woof")

dog = Dog()
dog.sound()