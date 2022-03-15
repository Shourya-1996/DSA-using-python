import numpy as np

twoDarray = np.array([[1, 2, 3, 12], [4, 5, 6, 11], [7, 8, 9, 14]])
# print(twoDarray)
newtwoDarray = np.insert(twoDarray, 3, [[1, 2, 3, 4]], axis=0)
print(newtwoDarray)


def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('incorrect index')
    else:
        print(array[rowIndex][colIndex])


accessElements(newtwoDarray, 2, 3)


def traverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


# traverse(newtwoDarray)

newarray = np.delete(newtwoDarray, 1, axis=0)
print(newarray)
