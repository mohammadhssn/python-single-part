"""
    queue
"""
import queue

q = queue.Queue()
# q = queue.LifoQueue()
# q = queue.PriorityQueue()

q.put(3)
q.put(10)
q.put(1)

print(q.get())
print(q.get())
print(q.get())
