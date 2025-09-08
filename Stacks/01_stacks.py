class Stacks:
    def __init__(self):
        self.stack=[]
        
    def push(self,element):
        self.stack.append(element)
    
    
    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            return "stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack)==0
    
    
    def size(self):
        return len(self.stack)
    
    
myStack = Stacks()

myStack.push(1)
myStack.push(4)
myStack.push(5)
myStack.push(7)
myStack.push(9)

print(myStack.stack)
print(myStack.pop())
print('stack after pop ',myStack.stack)
print(myStack.peek())
print(myStack.isEmpty())
print(myStack.size())