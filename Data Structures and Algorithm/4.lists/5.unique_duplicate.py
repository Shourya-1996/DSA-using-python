# is unique: implement an algorithm to determine if a list has all unique characters,using python list.

mylist = [1, 2, 3, 4, 5, 3, 3, 2, 4, 5, 6, 7, 10]


def isUnique(array):
    new = []
    for i in array:
        if i not in new:
            new.append(i)
        else:
            print(i)
            return False
    return True


print(isUnique(mylist))
