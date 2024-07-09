numlist = []
print("Enter total number of elements: \t")
n = int(input())
for i in range(1, n + 1):
    print("Enter element.")
    element = int(input())
    numlist.append(element)

    evenlist = []
    Oddlist = []

    for j in numlist:
        if j % 2 == 0:
            evenlist.append(j)
        else:
            Oddlist.append(j)

    print("Even numbers list \t: ", evenlist)
    print("Odd numbers list \t: ", Oddlist)

    