def selectionSort(arr):
    #loop through array
    for i in range(len(arr)):
        #set variable for our lowest value
        lowVal = i
        for j in range(i + 1, len(arr)):
            #compare and switch values
            if arr[j] < arr[lowVal]:
                lowVal = j
        arr[i], arr[lowVal] = arr[lowVal], arr[i]

#example data set
arr = [12, 8, 3, 20, 11]

selectionSort(arr)
print(arr)