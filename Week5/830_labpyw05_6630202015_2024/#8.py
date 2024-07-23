
#* 8. User-Defined

def even(x):
    return x%2==0 

def squared(x):
    return x*x

lst = [i for i in range(1,11)]
even_numbers = list(map(squared,filter(even,lst)))
print("Original list: ", lst)
print(even_numbers)