class Stack():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, val):
        self.items.append(val)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def front(self):
        return self.items[0]
    def rear(self):
        return self.items[-1]
stack = Stack()
stack.push(1)
stack.push(10)
stack.push(100)
print(stack.items)
print(stack.pop())
print(stack.items)
print(stack.front())
print(stack.rear())