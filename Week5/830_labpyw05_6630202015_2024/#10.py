
#* 10.

x = 99 # x is global variable  
def func(y):
    z = x + y 
    return z
print(func(1))

