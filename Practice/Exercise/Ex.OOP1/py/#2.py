
class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Puppy(Pet):
    def __init__(self, name, species, age):
        super().__init__(name, species)
        self.age = age

    def bark(self):
        return "Woof!"
    
    def introduce(self):
        return f"My name is {self.name}.\nI am species is {self.species} and age is {self.age} years old."

puppy = Puppy("Buddy", "Dog", 5)
print(puppy.bark())
print(puppy.introduce())

