
class ParentClass:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"ParentClass: {self.name}"

    def __eq__(self, other):
        if isinstance(other, ParentClass):
            return self.name == other.name
        return False

class ChildClass(ParentClass):
    def __str__(self):
        return f"ChildClass: {self.name}"

dog = ChildClass("Buddy")
print(dog) 

another_dog = ChildClass("Buddy")
print(dog == another_dog) 

