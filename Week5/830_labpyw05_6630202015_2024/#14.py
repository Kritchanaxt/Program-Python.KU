
#* 14.

def fun(s,num,d):
    s = "Hello"
    num = 10
    d = (5,6,7)
    print("Inside function call", s,num,d)

s = "Open genius"
num = 1
d = (1,2,3)
print("Before function call", s,num,d)
fun(s,num,d)
print("Outside function call", s,num,d)