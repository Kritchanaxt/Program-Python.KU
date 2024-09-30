
#? 2. Loop list of creating Dictionary

color = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
d = dict()
for color in color:
    key = len(color)
    if key not in d:
        d[key] = []
        d[key].append(color)
print(f"d: {d}")

