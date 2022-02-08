def bubbleSort(arr):
    for n in range(len(arr)-1, 0, -1):
        for i in range(n):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
arr = [39,12,18,85,72,10,2,18]

print("Unsorted list is,")
print(arr)
bubbleSort(arr)
print("Sorted Array is, ")
print(arr)
