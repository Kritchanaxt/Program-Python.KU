
#? 1. Write a program that creates the list [1,11,111,1111...,11.....1], where the entries have an ever increasing number of ones, with the last entry having 100 ones

class OneList:
    def __init__(self, length):
        self.length = length
        self.ones_list = []

    def create_ones_list(self):
        for i in range(1, self.length + 1):
            self.ones_list.append(int("1" * i))

    def display_list(self):
        for num in self.ones_list:
            print(num)


one_list = OneList(100)
one_list.create_ones_list()
one_list.display_list()
