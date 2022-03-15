def linearSearch(array, value):
    for i in array:
        if value == i:
            return array.index(i)
    return -1


arr = [1, 2, 3, 4, 5, 6, 7]
print(linearSearch(arr, 30))
