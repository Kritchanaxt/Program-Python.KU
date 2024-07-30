
#10.
value = []
items = [int(x) for x in input().split(',')]
result = " ".join(str(x) for x in items if x % 5 == 0) 
print(" ".join(result))