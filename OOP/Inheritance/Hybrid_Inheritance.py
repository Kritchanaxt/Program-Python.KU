
#? คลาส A → คลาส B, คลาส C; คลาส D สืบทอดจาก B และ C 

class A:
    def get_value(self):
        return 10

class B(A):
    def calculate(self):
        return self.get_value() * 2

class C(A):
    def calculate(self):
        return self.get_value() + 5

b = B()
result_b = b.calculate()
print(result_b)  

c = C()
result_c = c.calculate()
print(result_c)  

print("---------------------------------")

class BaseClass:
    def get_value(self):
        return 5

class ParentClass1(BaseClass):
    def get_multiplier(self):
        return 3

class ParentClass2(BaseClass):
    def get_additional(self):
        return 2

class ChildClass(ParentClass1, ParentClass2):
    def calculate(self):
        value = self.get_value()
        multiplier = self.get_multiplier()
        additional = self.get_additional()
        return (value * multiplier) + additional

child = ChildClass()
result = child.calculate()
print(result)  




