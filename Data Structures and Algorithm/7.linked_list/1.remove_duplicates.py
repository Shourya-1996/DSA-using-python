# write code to remove duplicates from an unsorted linked list
from LinkedList import LinkedList


def removeDups(ll):
    if ll.head is None:
        return
    else:
        currNode = ll.head
        visited = {currNode.value}  # created a set (or) set([currNode.value])
        while currNode.next:
            if currNode.next.value in visited:
                currNode.next = currNode.next.next
            else:
                visited.add(currNode.next.value)
                currNode = currNode.next
        return ll


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
removeDups(customLL)
print(customLL)
