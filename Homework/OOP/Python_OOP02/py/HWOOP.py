class Data:
    def __init__(self):
        self.age = []

    def inputAge(self, num):
        for i in range(num):
            self.age.append(int(input("Enter Age: ")))

    def printAllAge(self):
        return f"{self.age}"
    
    def findMax(self):
        return f"Max : {max(self.age)}"
    
    def findMin(self):
        return f"Min : {min(self.age)}"

    def CountAge(self):
        return f"Count : {len(self.age)}"
    
    def SumAge(self):
        return f"Summation : {sum(self.age)}"

CountOfLoop = int(input("Number loop: "))

data1 = Data()
data1.inputAge(CountOfLoop)

print(data1.printAllAge())
print(data1.findMax())
print(data1.findMin())
print(data1.CountAge())
print(data1.SumAge())
