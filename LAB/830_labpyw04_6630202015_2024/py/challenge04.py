
#? Challenge04

#! Method 1
n = 5
def pattern(n):
     for i in  range(n):
        num_start = 2 * i + 1
        print(' ' * (n - i - 1) + '*' * num_start)

pattern(n)

#! Method 2
n1 = 5
for i in range(n1):
    spaces = '  ' * (n - i - 1)
    stars = '*' * (2 * i + 1)
    print(spaces + stars)

#! Method 3
n2 = 5
for i in range(n2):
    print('*' * (2 * i + 1))