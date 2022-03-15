# how to check if an array contains a number in python

import numpy as np

myarray = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def findNumber(array, number):
    for i in range(len(array)):
        if array[i] == number:
            return i
    return 'number does not exist'


print(findNumber(myarray, 12))
