from multiprocessing import Queue

customQ = Queue(maxsize=3)
customQ.put(1)
print(customQ.get())
