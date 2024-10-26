
#? Ex.OOP1 - #1

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        return f"\nMy name is {self.name}. I am {self.age} years old.\n"
    
person1 = Person('BukGot', 60)
print(person1.introduce())