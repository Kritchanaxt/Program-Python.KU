
class Grandparent:
    def greet(self):
        return "Hello from Grandparent"

class Parent(Grandparent):
    def introduce(self):
        return "I am the Parent"

class Child(Parent):
    def say_name(self):
        return "I am the Child"

child = Child()
print(child.greet())        
print(child.introduce())    
print(child.say_name())      

print("---------------------------------")

class GrandparentClass:
    def get_value(self):
        return 10

class ParentClass(GrandparentClass):
    def get_multiplier(self):
        return 2

class ChildClass(ParentClass):
    def calculate(self):
        value = self.get_value()
        multiplier = self.get_multiplier()
        return value * multiplier

child = ChildClass()
result = child.calculate()
print(result)  
