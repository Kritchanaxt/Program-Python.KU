class Animal:
    def sound(self):
        print("Some animals make sounds")

class Dog(Animal):
    def sound(self):
        print("Dogs bark, woof, woof")

# Create an object from class Dog
dog = Dog()
dog.sound() # Call the sound method of class Dog