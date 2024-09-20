
class Parent1:
    def method1(self):
        return "Method from ParentClass1"

class Parent2:
    def method2(self):
        return "Method from ParentClass2"

class Child(Parent1, Parent2):
    def method3(self):
        return "Method from ChildClass"

child = Child()
print(child.method1())  
print(child.method2())  
print(child.method3()) 

print("---------------------------------")

class ParentClass1:
    def get_value(self):
        return 10

class ParentClass2:
    def get_multiplier(self):
        return 5

class ChildClass(ParentClass1, ParentClass2):
    def calculate(self):
        value = self.get_value()
        multiplier = self.get_multiplier()
        return value * multiplier

child = ChildClass()
result = child.calculate()
print(result)  

