from models.bubble import BubbleSort
from models.selectionSort import SelectSort

arr = [10, 65, 12, 1, 7, 69, 85, 11, 15, 42]

bubble = BubbleSort()
select = SelectSort()


sort = input("which sort would you like to use (type: bubble or select)?")


if sort == ("bubble"):
    print("unsorted array:")
    print(arr)

    print("sorted array:")
    bubble.bubbleSort(arr)
    print(arr)

elif sort == ("select"):
    print("unsorted array:")
    print(arr)

    print("sorted array:")
    select.selectionSort(arr)
    print(arr)