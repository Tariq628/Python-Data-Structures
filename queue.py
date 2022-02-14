class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, val):
        self.items.append(val)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def front(self):
        return self.items[0]
    def rear(self):
        return self.items[-1]
queue = Queue()
queue.enqueue(1)
queue.enqueue(10)
queue.enqueue(100)
print(queue.items)
print(queue.dequeue())
print(queue.front())
print(queue.rear())