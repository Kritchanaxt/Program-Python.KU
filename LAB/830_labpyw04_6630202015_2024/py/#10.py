
#? 10
counts = {'chuck' :1, 'annie' :2, 'jan' :3}
lst = list(counts.keys())
print(lst)
lst.sort()
for key in lst:
    print(key, counts[key])