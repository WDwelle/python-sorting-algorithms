from bubble import BubbleSort

arr = [10, 65, 12, 1, 7, 69, 85, 11, 15, 42]

bubble = BubbleSort()

print("unsorted array:")
print(arr)

print("sorted array:")
bubble.bubbleSort(arr)
print(arr)