# write a program to find all pairs of integers whose sum is equal to a given number.
# [2,3,5,6,9] --> 9 -->[3,6]
# distinct pairs

def findPairs(array, target):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                continue
            elif array[i] + array[j] == target:
                print(i, j)


mylist = [1, 2, 3, 4, 5, 6, 7, 8, 3, 4, 7]
findPairs(mylist, 6)
