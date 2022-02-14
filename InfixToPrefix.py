class Infix():
    def __init__(self):
        self.items = []
        self.precedence = {"+":1, "-":1, "*":2,"/":2, "^":3}
        self.output = []
    def push(self,val):
        self.items.append(val)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items==[]
    def isOperand(self, ch):
        return ch.isalpha()
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except Exception:
            return False
    def inf_to_pref(self, exp):
        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            else:
                while((not self.isEmpty() and self.notGreater(i))):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
        print("".join(self.output))

# Driver program to test above function 
exp = "a+b*c^d-e^f+g*h-i"
obj = Infix()
obj.inf_to_pref(exp)