
#* 6.

import math

c = 50
h = 30

items = input("Enter comma-separated numbers: ").split(',')

values = []
for d in items:
    q = (2 * c * float(d)) / h
    value = int(round(math.sqrt(q)))
    values.append(str(value))

print(values)
print(','.join(values))

