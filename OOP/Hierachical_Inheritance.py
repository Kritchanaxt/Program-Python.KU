
class MOM:
    def Mama(self):
        print("Mama")

class ChildOne(MOM):
    def Child(self):
        print("Child One")

class ChildTwo(MOM):
    def Child(self):
        print("Child Two")

child1 = ChildOne()
child2 = ChildTwo()
child1.Mama()  
child2.Mama() 
child1.Child()  
child2.Child()  

print("---------------------------------")

class ParentClass:
    def get_value(self):
        return 10

class ChildClass1(ParentClass):
    def calculate(self):
        return self.get_value() * 2

class ChildClass2(ParentClass):
    def calculate(self):
        return self.get_value() + 5

child1 = ChildClass1()
result1 = child1.calculate()
print(result1)  

child2 = ChildClass2()
result2 = child2.calculate()
print(result2)  
