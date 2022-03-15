from array import *

arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [2.1, 4.1, 4.4])

# print(arr1)

#arr1.insert(6, 9)
# arr1.insert(0, 0)
arr1.insert(3, 8)
# print(arr1)


def traverseArray(array):
    for i in array:
        print(i)


# traverseArray(arr1)


def accessElementl(array, index):
    if index >= len(array):
        print('there is not any element in this index')
    else:
        print(array[index])


# accessElement(arr1, 2)
# print(len(arr1))

def searchInArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return 'not found in array'


# print(searchInArray(arr1, ))
arr1.remove(5)
# print(arr1)
