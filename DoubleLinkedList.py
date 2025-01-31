class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)
    
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result
    
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length +=1
    
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        
    def traverse(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
            
    def reverse_traverse(self):
        temp_node = self.tail
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.prev

    def search(self,value):
        temp_node = self.head
        index = 0
        while temp_node is not None:
            if temp_node.value == value:
                return f"{value} at {index}"
            temp_node = temp_node.next
            index += 1
        return False
    
    def get(self,index):
        if index < 0 or index >= self.length:
            return None
        elif index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node
    
    def set(self,index, value):
        if index < 0 or index >= self.length:
            return None
        elif index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            current_node.value = value
        else:
            current_node = self.tail
            for _ in range(self.length-1,index,-1):
                current_node = current_node.prev
            current_node.value = value
        return current_node.value
    
    def insert(self,index,value):
        new_node = Node(value)
        if index < 0 or index >= self.length + 1:
            return None
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == self.length:
            self.append(value)
            return 
        elif index == 0:
            self.prepend(value)
            return
            
        elif index < self.length // 2:
            current_node = self.head
            for _ in range(index-1):
                current_node = current_node.next
            new_node.next = current_node.next
            new_node.prev = current_node
            new_node.next.prev = new_node
            current_node.next = new_node
            self.length += 1
        else:
            current_node = self.tail
            for _ in range(self.length -1 , index , -1):
                current_node = current_node.prev
            new_node.prev = current_node.prev
            new_node.next = current_node
            current_node.prev.next = new_node
            current_node.prev = new_node
            self.length += 1
    
    def pop_first(self):
        if self.head is None:
            return "Empty List"
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            popped_node = self.head
            self.head = popped_node.next
            popped_node.next = None
            self.head.prev = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        if self.head is None:
            return "Empty List"
        elif self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
        else:
            popped_node = self.tail
            self.tail = popped_node.prev
            popped_node.prev = None
            self.tail.next = None
        self.length -= 1
        return popped_node
    
    def remove(self,index):
        if index < 0 or index >= self.length:
            return "Invalid Index"
        elif self.head is None:
            return "Empty List"
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        elif index < self.length+1 // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            popped_node = current_node
            current_node.prev.next = current_node.next
            current_node.next.prev = popped_node.prev
            popped_node.next = None
            popped_node.prev = None
        else:
            current_node = self.tail
            for _ in range(self.length -1 , index , -1):
                current_node = current_node.prev
            popped_node = current_node
            current_node.prev.next = current_node.next
            current_node.next.prev = popped_node.prev
            popped_node.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node
            
new_linked_list = DoubleLinkedList()
new_linked_list.append(1)
new_linked_list.append(2)
new_linked_list.append(3)
new_linked_list.append(4)
print(new_linked_list)
print(new_linked_list.length)
new_linked_list.prepend(0)
print(new_linked_list)
new_linked_list.traverse()
new_linked_list.reverse_traverse()
print(new_linked_list.search(1))
print((new_linked_list.length + 1) // 2)
print(new_linked_list.get(-3))
# print(new_linked_list.set(4,5))
print(new_linked_list)
new_linked_list.insert(0,4)
new_linked_list.insert(6,4)
print(new_linked_list)
print(new_linked_list.length)
print(new_linked_list.pop_first())
print(new_linked_list)
print(new_linked_list.length)
print(new_linked_list.pop())
print(new_linked_list.remove(3))
print(new_linked_list)
print(new_linked_list.length)
