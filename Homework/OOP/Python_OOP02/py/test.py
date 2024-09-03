
class Data:
    def __init__(self):
        self.age = []

    def inputAge(self,num):
        for i in range(num):
            data = int(input("Enter Age: "))
            self.age.append(data)

    def printAllAge(self):
        return f"{self.age}"
    
    def findMax(self):
        max_value = self.age[0]  
        for i in range(0, len(self.age)):
            if max_value < self.age[i]:
                max_value = self.age[i]
        return f"Max : {max_value}"
    
    def findMin(self):
        min_value = self.age[0]
        for i in range(0,len(self.age)):
            if min_value > self.age[i]:
                min_value = self.age[i]
        return f"Min : {min_value}"

    def CountAge(self):
        count= len(self.age)
        return f"Count : {count}"
    
    def SumAge(self):
        Summm = 0
        for i in range(0,len(self.age)):
            Summm += self.age[i]

        return f"Summation : {Summm}"
    
CountOfLoop = int(input("Number loop :"))

data1 = Data()
data1.inputAge(CountOfLoop)

print(data1.printAllAge())

print(data1.findMax())
print(data1.findMin())
print(data1.CountAge())
print(data1.SumAge())