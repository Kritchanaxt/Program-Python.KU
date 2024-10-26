
#? Python_OOP06

class DivisibleBySeven:
    def __init__(self, limit):
        self.limit = limit
        self.result = []

    def find_number(self):
        for i in range(1, self.limit + 1):
            if i % 7 == 0 and str(i)[-1] == "6":
                self.result.append(i)

    def display_number(self):
        for num in self.result:
            print(num)

seven_checker = DivisibleBySeven(1000)
seven_checker.find_number()
seven_checker.display_number()