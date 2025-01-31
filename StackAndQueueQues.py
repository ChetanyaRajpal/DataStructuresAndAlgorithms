class MultiStack:
    def __init__(self, stacksize):
        self.stacksize = stacksize
        self.numberstacks = 3
        self.items = [0] * (self.stacksize * self.numberstacks)
        self.sizes = [0] * self.numberstacks
        
    def __str__(self):
        result = ''
        counter = 0
        stack_num = 0
        result += (f"Current Stack : {stack_num}\n")
        
        for i in self.items:
            result += str(i)
            result += '\n'
            counter += 1
            if counter == self.stacksize:
                stack_num += 1
                result += f"Current Stack : {stack_num}"
                result += '\n'
                counter = 0
        return result
            
        
    def isFull(self,numstack):
        if self.sizes[numstack] == self.stacksize:
            return True
        else:
            return False
    
    def isEmpty(self,numstack):
        if self.sizes[numstack] == 0:
            return True
        else:
            return False
        
    def indexOfTop(self,stacknum):
        offset = self.stacksize * stacknum
        return offset + self.sizes[stacknum]-1

    def push(self,item,stacknum):
        if self.isFull(stacknum):
            print(f"Number {stacknum} stack is full")
        else:
            self.sizes[stacknum] += 1
            self.items[self.indexOfTop(stacknum)] = item
            
    def pop(self,stacknum):
        if self.isEmpty(stacknum):
            print(f"Number {stacknum} stack is empty.")
        else:
            self.sizes[stacknum] -= 1
            value = self.items[self.indexOfTop(stacknum)]
            print(f"The popped item is : {value}")
            self.items[self.indexOfTop(stacknum)] = 0 
               
    def peek(self,stacknum):
        if self.isEmpty(stacknum):
            print(f"Number {stacknum} stack is empty.")
            
        else:
            value = self.items[self.indexOfTop(stacknum)]
            print(value)
            
new_stack = MultiStack(3)
new_stack.push(5,0)
new_stack.push(6,0)
new_stack.push(6,1)
new_stack.push(6,1)
new_stack.push(6,2)
new_stack.push(6,2)
print(new_stack)

class Node:
    def __init__(self,value = None ,next = None):
        self.value = value
        self.next = next
    
    def __str__(self):
        string = str(self.value)
        if self.next:
            string += str(self.next)
        return string
    
class Stack:
    def __init__(self):
        self.top = None
        self.minNode = None
        
    def __str__(self):
        result1 = ''
        result2 = ''
        min_node_pointer = self.minNode
        top_pointer = self.top
        while top_pointer:
            result1 += str(top_pointer.value) 
            if top_pointer.next:
                result1 += ' -> '
            top_pointer = top_pointer.next
        while min_node_pointer:
            result2 += str(min_node_pointer.value)
            if min_node_pointer.next:
                result2 += ' -> '
            min_node_pointer = min_node_pointer.next
        return result1
    
    def min(self):
        if self.minNode == None:
            return "The list is Empty"
        else:
            return self.minNode.value
        
    def push(self,value):
        if self.minNode and (self.minNode.value < value):
            self.minNode = Node(value = self.minNode.value, next = self.minNode)
            self.top = Node(value = value, next = self.top)
        else:
            self.minNode = Node(value = value, next = self.minNode)
            self.top = Node(value = value, next = self.top)
    
    def pop(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            self.minNode = self.minNode.next
            item = self.top.value
            self.top = self.top.next
            return item
        
new_stack = Stack()
new_stack.push(5)
new_stack.push(7)
new_stack.push(7)
new_stack.push(4)
print(new_stack.pop())
print(new_stack)

class PlateStack:
    def __init__(self,capacity):
        self.capacity = capacity
        self.items = []
        
    def __str__(self):
        return str(self.items)
    
    def push(self,value):
        if len(self.items) > 0 and len(self.items[-1]) < self.capacity:
            self.items[-1].append(value)
        else:
            self.items.append([value])

    def pop(self):
        while len(self.items) and len(self.items[-1]) == 0:
            self.items.pop()
        if len(self.items) == 0:
            return None
        else:
            self.items[-1].pop()
            
    def popAt(self,stackNumber):
        if self.items[stackNumber] > 0:
            return self.items[stackNumber].pop()
        else:
            return None
        
new_stack = PlateStack(2)
new_stack.push(3)
new_stack.push(3)
new_stack.push(5)
new_stack.pop()
print(new_stack)

class Stack2:
    def __init__(self):
        self.list = []
    def __len__(self):
        return len(self.list)
    def push(self,value):
        self.list.append(value)
    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            self.list.pop()
            
class QueueviaStack:
    def __init__(self):
        self.instack = Stack2()
        self.outstack = Stack2()
    
    def instack(self):
        result = [str(x) for x in self.instack]
        return '\n'.join(result)
    
    def outstack(self):
        result = [str(x) for x  in self.outstack]
        return '\n'.join(result)
    
    def enqueue(self,value):
        self.instack.push(value)
        
    def dequeue(self):
        while len(self.instack):
            self.outstack.push(self.instack.pop())
        result = self.outstack.pop()
        while len(self.outstack):
            self.instack.push(self.outstack.pop())
        return result