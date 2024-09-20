
class ParentClass:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class ChildClass(ParentClass):
    def speak(self):
        return f"{self.name} barks"

dog = ChildClass("Buddy")
print(dog.speak())
