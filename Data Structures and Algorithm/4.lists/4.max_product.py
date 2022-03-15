# how to find maximum product of two integers in a array where all elements are positive
import numpy as np

myarray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def maxProduct(array):
    product = 1
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if product <= array[i]*array[j]:
                product = array[i]*array[j]
                pairs = f"pair = ({array[i]} , {array[j]})"
            else:
                continue
    print(pairs)
    print(product)


maxProduct(myarray)
