
#? StaticMethod

class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
result_add = MathOperations.add(5, 3)
result_multiply = MathOperations.multiply(4, 6)

print("Add:", result_add)
print("Multiply:", result_multiply)