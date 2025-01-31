class Queue:
    def __init__(self):
        self.items = []
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False
        
    def enqueue(self,value):
        self.items.append(value)
        print(f"The item has been inserted at the end of the queue {value}")
        
    def dequeue(self):
        if self.isEmpty():
            print("The queue is Empty")
        else:
            popped = self.items.pop(0)
            print(f"The item has been removed from the queue {popped} ")
            
    def peek(self):
        if self.isEmpty():
            print("The queue is Empty")
        else:
            print(self.items[0])
            
    def delete(self):
        self.items = []
        
new_queue = Queue()
new_queue.enqueue(5)
new_queue.enqueue(7)
print(new_queue)
# new_queue.dequeue()
(new_queue.peek())

class CircularQueue:
    def __init__(self,max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1
        
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        if self.start == self.top + 1:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def Enqueue(self,value):
        if self.isFull():
            print("Queue is Full")
        else:
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            print(f"The item has been inserted in the queue {value}")
            
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            print(f"The first element has been removed from the queue {firstElement}")
            
    def peek(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print(self.items[self.start])
            
    def delete(self):
        self.items = self.max_size * [None]
        self.top = -1
        self.start = -1
    
new_queue1 = CircularQueue(5)
new_queue1.Enqueue(5)
new_queue1.Enqueue(7)
new_queue1.Enqueue(8)
print(new_queue1)
print(new_queue1.start)
print(new_queue1.top)
new_queue1.Dequeue()
print(new_queue1)
print(new_queue1.start)
print(new_queue1.top)
(new_queue1.peek())

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next
            
class LinkedListQueue:
    def __init__(self):
        self.items = LinkedList()
        
    def __str__(self):
        current_node = self.items.head
        result = ''
        while current_node:
            result += str(current_node.value)
            if current_node.next:
                result += ' -> '
            current_node = current_node.next
        return result
    
    def Enqueue(self,value):
        new_node  = Node(value)
        if self.items.head is None:
            self.items.head = new_node
            self.items.tail = new_node
        else:
            self.items.tail.next = new_node
            self.items.tail = new_node
            
    def Dequeue(self):
        if self.items.head is None:
            print("The Queue is Empty")
        else:
            if self.items.head == self.items.tail:
                removed_node = self.items.head
                self.items.head = None
                self.items.tail = None
            else:
                removed_node = self.items.head
                self.items.head = self.items.head.next
                removed_node.next = None
            print(f"An Item from the Queue has been successfully removed : {removed_node.value}")
    
    def isEmpty(self):
        if self.items.head is None:
            return True
        else:
            return False
        
    def peek(self):
        if self.items.head is None:
            print("The Queue is Empty")
        else:
            print(self.items.head.value)
            
    def delete(self):
        self.items.head = None
        self.items.tail = None
    
new_queue2 = LinkedListQueue()
new_queue2.Enqueue(5)
new_queue2.Enqueue(7)
new_queue2.Dequeue()
print(new_queue2)
        
from collections import deque
new_queue3 = deque(maxlen=3)
new_queue3.append(5)
new_queue3.append(7)
print(new_queue3)

import queue as q
new_queue4 = q.Queue(maxsize=3)
new_queue4.put(4)
new_queue4.put(5)
new_queue4.put(7)
print(new_queue4.full())

from multiprocessing import Queue
new_queue5 = Queue(maxsize = 3)

