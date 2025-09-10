class Queue:
    def __init__(self):
        self.queue =[]
    
    def enqueue(self,element):
        self.queue.append(element)
    
    def dequeue(self):
        if self.isEmpty():
            return 'Queue is empty'
        return self.queue.pop(0)
    
    def isEmpty(self):
        return len(self.queue) ==0
    
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if self.isEmpty():
            return 'queue is empty'
        return self.queue[0]
    
    
myqueue = Queue()

myqueue.enqueue(1)
myqueue.enqueue(2)
myqueue.enqueue(3)
myqueue.enqueue(6)
myqueue.enqueue(7)
myqueue.enqueue(4)

print(myqueue.queue)
print(myqueue.peek())
print(myqueue.dequeue())
print(myqueue.queue)
print(myqueue.isEmpty())
print(myqueue.size())

            