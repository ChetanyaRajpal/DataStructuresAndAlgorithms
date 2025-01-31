class Stack:
    def __init__(self):
        self.list = []
        
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self,value):
        self.list.append(value)
        print(f"Push Successful {value}")
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.list.pop()   
        
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.list[len(self.list) - 1]
        
    def delete(self):
        self.list = None
        
class LimitStack:
    def __init__(self,max_size):
        self.max_size = max_size
        self.list = []
        
    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list) == self.max_size:
            return True
        else:
            return False
        
    def push(self,value):
        if self.isFull():
            print("The stack is full")
        else:
            self.list.append(value)
            print(f"Push Successful {value}")
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.list.pop()   
        
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            return self.list[len(self.list) - 1]
        
    def delete(self):
        self.list = None
        
        
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next
            
class LinkedListStack:
    def __init__(self):
        self.list = LinkedList()
        
    def __str__(self):
        current_node = self.list.head
        result = ''
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node:
                result += '\n'
        return result
    
    def push(self,value):
        new_node = Node(value)
        if self.list.head is None:
            self.list.head = new_node    
        else:
            new_node.next = self.list.head
            self.list.head = new_node
    
    def isEmpty(self):
        if self.list.head is None:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            popped_node = self.list.head
            self.list.head = self.list.head.next
            popped_node.next = None
            print(f"Popped Node : {popped_node.value}")
            
    def peep(self):
        if self.isEmpty():
            print("Stack is Empty")
        else:
            print(self.list.head)
            
    def delete(self):
        self.list.head = None
    
            
new_stack = Stack()
print(new_stack.isEmpty())
new_stack.push(5)
new_stack.push(7)
new_stack.push(8)
print(new_stack)
new_stack.pop()
print(new_stack)
print(new_stack.peek())
new_stack1= LimitStack(3)
print(new_stack.isEmpty())
new_stack1.push(5)
new_stack1.push(7)
new_stack1.push(8)
print(new_stack1)
# new_stack.pop()
print(new_stack1)
print(new_stack1.peek())
print(new_stack1.isFull())
new_stack2 = LinkedListStack()
new_stack2.push(5)
new_stack2.push(7)
new_stack2.push(9)
print(new_stack2)
new_stack2.pop()
print(new_stack2)
new_stack2.peep()