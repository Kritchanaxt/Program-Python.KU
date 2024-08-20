
#* 6. Sort Numbers in a List Using Bubble Sort

numbers = list(map(int, input("Enter numbers: ").split()))

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

bubble_sort(numbers)
print("Sorted list:", numbers)
