class ParentClass:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"ParentClass: {self.name}"
    
    def __repr__(self):
        return f"ParentClass(name={self.name})"
    
    def __eq__(self, other):
        if isinstance(other, ParentClass):
            return self.name == other.name
        return False
    
    def __len__(self):
        return len(self.name)
    
    def __hash__(self):
        return hash(self.name)
    
    def __del__(self):
        print(f"Deleting {self.name}")

class ChildClass(ParentClass):
    def __str__(self):
        return f"ChildClass: {self.name}"
    
    def __add__(self, other):
        if isinstance(other, ChildClass):
            return ChildClass(self.name + other.name)
    
    def __call__(self):
        print(f"{self.name} has been called!")
    
    def __getitem__(self, index):
        return self.name[index]
    
    def __setitem__(self, index, value):
        temp = list(self.name)
        temp[index] = value
        self.name = ''.join(temp)

dog = ChildClass("Buddy")
print(dog)

another_dog = ChildClass("Buddy")
print(dog == another_dog)

print(len(dog))

print(hash(dog))

combined_dog = dog + another_dog
print(combined_dog)

dog()

print(dog[2])

dog[2] = 'Z'
print(dog)

del dog
