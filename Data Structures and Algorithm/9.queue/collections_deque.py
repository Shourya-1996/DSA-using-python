from collections import deque

customQ = deque(maxlen=3)
print(customQ)
customQ.append(1)
customQ.append(2)
customQ.append(3)
print(customQ)
customQ.append(4)  # if queue is full it will overwrite the first value
print(customQ)
print(customQ.popleft())
print(customQ)
customQ.clear()
print(customQ)
