class Queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.q.pop(0)
        else:
            raise IndexError("Cannot dequeue from an empty queue")

    def size(self):
        return len(self.q)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size()) 

while not queue.is_empty():
    print("Dequeued:", queue.dequeue())