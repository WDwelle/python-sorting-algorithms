    
class BubbleSort:

    def bubbleSort(self, arr):
        n = len(arr)

        for i in range(n-1):

            for j in range(0, n-i-1):

                if arr[j] > arr[j + 1] :
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

    #example input
    #arr = [39,12,18,85,72,10,2,18]

    #starting data
    #print("Unsorted list is,")
    #print(arr)
    #bubbleSort(arr)
    #ending data
    #print("Sorted Array is, ")
    #print(arr)
