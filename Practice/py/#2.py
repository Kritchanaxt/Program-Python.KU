
#? Hybrid_Inheritance

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
