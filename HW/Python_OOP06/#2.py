
#? 2. Write a program to find all numbers between 1 and 1000 that are divisible by 7 and end in a 6.

class DivisibleBySeven:
    def __init__(self, limit):
        self.limit = limit
        self.result = []

    def find_numbers(self):
        for i in range(1, self.limit + 1):
            if i % 7 == 0 and str(i)[-1] == "6":
                self.result.append(i)

    def display_numbers(self):
        for num in self.result:
            print(num)


seven_checker = DivisibleBySeven(1000)
seven_checker.find_numbers()
seven_checker.display_numbers()
