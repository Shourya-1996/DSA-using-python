import math


def binarySearch(array, value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)
    while not(array[middle] == value) and start <= end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
        middle = math.floor((start+end)/2)
    if array[middle] == value:
        return middle
    else:
        return -1


custArr = [1, 2, 3, 4, 5, 6, 6, 7, 8]
print(binarySearch(custArr, 30))
