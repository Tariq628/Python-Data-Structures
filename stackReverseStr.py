class Stack():
    def __init__(self):
        self.items = []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items == []

    def reverseStr(self, data_str):
        return data_str[::-1]
        reverse = ""
        for i in data_str:
            self.push(i)
        while (not self.isEmpty()):
            reverse += self.pop()
        return reverse
stack = Stack()
print(stack.reverseStr("world"))