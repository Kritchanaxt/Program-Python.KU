
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}. I am {self.age} years old."
    
person1 = Person('Got', 60)
print(person1.introduce())

