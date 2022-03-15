# write a code to return the Nth node value from the last of a linked list.
from LinkedList import LinkedList


def nthToLast(ll, n):
    pointer1 = ll.head
    pointer2 = ll.head

# moving pointer2 n distance from pointer1
    for i in range(n):
        if pointer2 is None:
            return None
        pointer2 = pointer2.next
# moving both pointers simulaneously till pointer2 reaches last node
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(nthToLast(customLL, 3))
