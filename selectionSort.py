def selectionSort(arr):
    for i in range(len(arr)):
        lowVal = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[lowVal]:
                lowVal = j
        arr[i], arr[lowVal] = arr[lowVal], arr[i]


random_list_of_nums = [12, 8, 3, 20, 11]
selectionSort(random_list_of_nums)
print(random_list_of_nums)