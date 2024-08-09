
#* 5.

def swap(x,y):
    return y,x

x = 10
y = 20
print(f'Before swap: {x=}, {y=}')
x,y = swap(x,y)
print(f'After swap: {x=}, {y=}')