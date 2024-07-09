
#! 5.

#output --> ['cody', 'aaron', 'bernice']
students = ['bernice', 'aaron', 'cody']
a = len(students)
print(a)
b = 0
#print(student[i])
while b < a:
    print(students[b])
    b += 1

print('\n')

for x in range(a):
    print(students[x])

b = len(students) -1

print('While - Reverse')

#Critical Thinking
while b >= 0:
    print(students[b])
    b -= 1

#Reverse --> WHilel --for
c = len(students)-1
for i in range(len(students)):
    print(students[c])
    c -= 1  # remove


