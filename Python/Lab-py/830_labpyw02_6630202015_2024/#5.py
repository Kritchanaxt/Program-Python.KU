
#? 5. Sum

count = 0 
sum = 0
print('Before', count, sum)
for i in [9, 41, 3, 74, 15]:
    # sum = 0
    count += 1
    sum += i
    print(count, sum, i)
print('After', count, sum, sum/count)