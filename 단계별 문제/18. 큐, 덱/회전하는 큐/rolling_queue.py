import sys
from collections import deque

class CircleQueue:
    rear = 0
    front = 0
    MAX_SIZE = 10
    queue = deque()

    def __init__(self):
        self.rear = 0
        self.front = 0
        self.queue = [0 for i in range(self.MAX_SIZE)]
    
    def is_empty(self):
        if self.rear==self.front:
            return True
        return False
    
    def is_full(self):
        if(self.rear+1)%self.MAX_SIZE==self.front:
            return True
        return False
    
    def enqueue(self, x):
        if not self.is_full():
            self.rear = (self.rear+1)%self.MAX_SIZE
            self.queue[self.rear] = x
    
    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front+1)%self.MAX_SIZE
            return self.queue[self.front]

    def peek(self):
        if not self.is_empty():
            return self.queue[(self.front+1)%self.MAX_SIZE]

    def print(self):
        out = []
        if self.front < self.rear:
            out = self.queue[self.front+1 : self.rear+1]
        else:
            out = self.queue[self.front+1 : self.MAX_SIZE] + self.queue[0:self.rear+1]
        print(self.rear, self.front, out)

cq = CircleQueue()
for i in range(10):
    cq.enqueue(i)

cq.print()