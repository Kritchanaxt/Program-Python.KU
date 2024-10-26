
#? Ex.OOP1 - #2

class Pet: 
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Puppy(Pet):
    def __init__(self, name, species, age):
        super().__init__(name, species)
        self.age = age

    def bark(self):
        return "\nWoof!"
    
    def introduce(self):
        return f"My name is {self.name}. I am species is {self.species} and age is {self.age} years old.\n"
    
puppy = Puppy("Buddy", "Dog", 5)
print(puppy.bark())
print(puppy.introduce())