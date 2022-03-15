# You have two numbers represented by a linked list where each node contains a single digit.
# The digits are stored in reverse order, such that the 1st digit is at the head of list.
# write a code that adds these two numbers and return the sum as a linked list
from LinkedList import LinkedList
import math


def sumList(llA, llB):
    n1 = llA.head
    n2 = llB.head
    carry = 0
    ll = LinkedList()

    numA = 0
    x = 0
    while n1:
        numA += n1.value*pow(10, x)
        n1 = n1.next
        x += 1

    numB = 0
    x = 0
    while n2:
        numB += n2.value*pow(10, x)
        n2 = n2.next
        x += 1
    sumAB = numA+numB
    length = len(str(sumAB))

    n1 = llA.head
    n2 = llB.head
    for i in range(length):
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next
        if n2:
            result += n2.value
            n2 = n2.next
        ll.add(int(result % 10))
        carry = result/10

    return ll


llA = LinkedList()
llA.add(7)
llA.add(7)
llA.add(7)
llA.add(7)
llA.add(7)
print(llA)
llB = LinkedList()
llB.add(2)
llB.add(3)
llB.add(7)
print(llB)
print(sumList(llA, llB))
