def missing_number(array, n):
    sum1 = n*(n+1)/2
    sum2 = sum(array)
    if sum1 == sum2:
        return 'No number is missing'
    else:

        return sum1-sum2


mylist = [1, 2, 3, 4, 5, 7, 8, 9, 10]
print(missing_number(mylist, 10))
