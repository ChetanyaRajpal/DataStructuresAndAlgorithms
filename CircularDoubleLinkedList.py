class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None
        
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
            result += ' <-> '
        return result
        
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length += 1
        
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.tail.next = self.head
        self.length += 1

    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index >= self.length + 1:
            return "Out of Order"
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        elif index <= self.length // 2:
            current_node = self.head
            for _ in range(index-1):
                current_node = current_node.next
            new_node.prev = current_node
            new_node.next = current_node.next
            current_node.next.prev = new_node
            current_node.next = new_node
        else:
            current_node = self.tail
            for _ in range(self.length-1,index, -1):
                current_node = current_node.prev
            new_node.next = current_node
            new_node.prev = current_node.prev
            current_node.prev.next = new_node
            current_node.prev = new_node
        self.length += 1
        
    def traverse(self):
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next
            if current_node == self.head:
                break

    def reverse_traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node)
            current_node = current_node.prev
            if current_node == self.tail:
                break
    
    def search(self,target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return f"{target} at {index}"
            current_node = current_node.next
            if current_node == self.head:
                break
            index += 1
        return False
                
    def get(self,index):
        if index < 0 or index >= self.length:
            return "Out of Order"
        elif index <= (self.length) // 2:
            current_node = self.head
            for _ in range(0, index):
                current_node = current_node.next
            return current_node
        else:
            current_node = self.tail
            for _ in range(self.length-1, index, -1):
                current_node = current_node.prev
            return current_node
        
    def set(self,index, value):
        current_node = self.get(index)
        current_node.value = value
        return current_node
    
    def pop_first(self):
        if self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        elif self.length == 0:
            return "Empty"
        else:
            popped_node = self.head
            self.head.next.prev = self.tail
            self.tail.next = self.head.next
            self.head = self.head.next
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        elif self.length == 0:
            return "Empty"
        else:
            popped_node = self.tail
            self.tail = popped_node.prev
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return popped_node
    
    def remove(self,index):
        if index < -1 or index >= self.length:
            return "Invalid Index"
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        elif index == -1:
            return self.pop()
        elif index <= self.length // 2:    
            popped_node = self.head
            for _ in range(index):
                popped_node = popped_node.next
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.next = None
            popped_node.prev = None
            
        else:
            popped_node = self.tail
            for _ in range(self.length - 1, index , -1):
                popped_node = popped_node.prev
            popped_node.prev.next = popped_node.next
            popped_node.next.prev = popped_node.prev
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
        
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)
print(new_linked_list.head.prev)
new_linked_list.prepend(20)
new_linked_list.prepend(5)
print(new_linked_list)
print(new_linked_list.head.prev)
print(new_linked_list.tail.next)
print(new_linked_list.length)
new_linked_list.insert(5,1)
print(new_linked_list)
# new_linked_list.traverse()
# new_linked_list.reverse_traverse()
print(new_linked_list.search(30))
print(new_linked_list.get(5))
print(new_linked_list.set(3,50))
print(new_linked_list)
# print(new_linked_list.pop_first())
print(new_linked_list)
print(new_linked_list.remove(5))
print(new_linked_list)

