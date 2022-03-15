# write a code to partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater than equal to x.
from LinkedList import LinkedList


def partition(ll, x):
    currentNode = ll.head
    ll.tail = ll.head

    while currentNode:
        nextNode = currentNode.next
        currentNode.next = None
        if currentNode.value < x:
            currentNode.next = ll.head
            ll.head = currentNode
        else:
            ll.tail.next = currentNode
            ll.tail = currentNode
        currentNode = nextNode
# if all the nodesvalues is less than x
    if ll.tail.next is not None:
        ll.tail.next = None
    return ll


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(partition(customLL, 50))
