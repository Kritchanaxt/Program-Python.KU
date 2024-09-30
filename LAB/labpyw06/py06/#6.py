
#6.

s = input()
dic = {word:s.count(word) for word in s}
for k, v in dic.items():
    print(f'{k}: {v}')