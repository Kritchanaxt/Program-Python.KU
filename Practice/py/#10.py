
#? Overriding

class Animal:
    def sound(self):
        print("Some animals make sounds")

class Dog(Animal):
    def sound(self):
        print("Dogs bark, woof, woof")

dog = Dog()
dog.sound()