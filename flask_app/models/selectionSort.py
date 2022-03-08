# -*- coding: UTF-8 -*-
class SelectSort:

    def selectionSort(self, arr):
        #print("Running Selection sort")
        #loop through array
        for i in range(len(arr)):
            #set variable for our lowest value
            lowVal = i
            for j in range(i + 1, len(arr)):
                #compare and switch values
                if arr[j] < arr[lowVal]:
                    lowVal = j
            arr[i], arr[lowVal] = arr[lowVal], arr[i]