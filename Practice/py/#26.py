
#? Test #2

def combine(current, n):
    if n == 0:
        print(current)
    else:
        combine(current + "H", n - 1)
        combine(current + "T", n - 1)
    
combine("", 3)