
#* 9.

lines = []
while True:
    s = input("Enter lines:")
    if s: 
        lines.append(s.upper())
    else: 
        break;

for sentence in lines:
    print(sentence)