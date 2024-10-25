
#? Overloading

class Calculator:
    def add(self, x=None, y=None, z=None):
        if x != None and y != None and z != None:
            return x + y + z
        elif x != None and y != None:
            return x + y
        elif x != None:
            return x
        else:
            return 0
        
cal = Calculator()

print(cal.add(5, 10, 15))
print(cal.add(5, 10))
print(cal.add(5))
print(cal.add())