class Stack:
    def __init__(self):
        self.st = []

    def is_empty(self):
        return len(self.st) == 0
 
    def push(self, item):
        self.st.append(item)

    def pop(self):
        if not self.is_empty():
            return self.st.pop()
        else:
            raise IndexError("Cannot pop from an empty stack")

    def peek(self):
        if not self.is_empty():
            return self.st[-1]
        else:
            raise IndexError("Cannot peek into an empty stack") 

    def size(self):
        return len(self.st)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Top element:", stack.peek())
 
while not stack.is_empty():
    print("Popped:", stack.pop())