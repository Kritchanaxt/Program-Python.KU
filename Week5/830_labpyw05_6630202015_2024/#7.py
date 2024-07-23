
#* 7.
lst=[i for i in range(1,11)]
even_numbers = list(map(lambda x: x**2, filter(lambda x: x%2==0, lst)))
print("Original list: ", lst)
print(even_numbers)