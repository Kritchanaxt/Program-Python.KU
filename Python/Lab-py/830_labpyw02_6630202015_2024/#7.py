#7. Min
min_so_far = 10000
print('Before', min_so_far)
for i in [9,41,12,3,74,15]:
    if i < min_so_far:
        min_so_far = i 
    print(min_so_far)
print('After', min_so_far)