class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        my_emty_str = ''
        temp_node = self.head
        while temp_node:
            my_emty_str += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            my_emty_str += " => "
        return my_emty_str
        
    def prepend(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
        
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            new_node.next = new_node
            self.tail = new_node
            self.length += 1
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    
    def insert(self,value,index):
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        elif self.length == 0:
            self.append(value)
        else:
            new_node = Node(value)
            prev_node = self.head
            index_here = 0
            while index_here != index-1:
                prev_node = prev_node.next
                index_here += 1
            next_node = prev_node.next
            prev_node.next = new_node
            new_node.next = next_node
            self.length += 1
    
    def traverse(self):
        temp_node = self.head
        while temp_node:
            print(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
    
    def search(self, value):
        temp_node = self.head
        index = 0
        while temp_node:
            if temp_node.value == value:
                print(f"{value} at {index}")
                break
            else:
                temp_node = temp_node.next
                index += 1
                if temp_node == self.head:
                    print("not found")
                    break
                
    def get(self,index):
        temp_node = self.head
        if index >= self.length:
            print("index out of range")
        elif index < -1:
            print("index out of range")
        elif index == -1:
            print(self.tail.value)
        else:
            for _ in range(index):
                    temp_node = temp_node.next
            print(temp_node.value)

    def set(self,index,value):
        temp_node = self.head
        if index < -1 or index >= self.length:
            return "Out of range"
        elif index == -1:
            self.tail.value = value
            return self.tail.value
        else:
            for _ in range(index):
                temp_node = temp_node.next
            temp_node.value = value
            return temp_node.value
        
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.head == None:
            return "List Empty"
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node.value
    
    def pop(self):
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        elif self.head == None:
            return "List Empty"
        else:
            temp_node = self.head
            for _ in range(self.length-2):
                temp_node = temp_node.next
            temp_node.next = self.tail.next
            self.tail = temp_node
            popped_node.next = None
        self.length -= 1
        return popped_node.value

    def remove(self,index):
        popped_node = None
        prev_node = self.head
        if index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        elif index == -1:
            return self.pop()
        elif index < -1 or index >= self.length:
            return "Out of Order"
        elif self.length == 1:
            self.head = None
            self.tail = None
            return prev_node.value
        elif self.length == 0:
            return "List Empty"
        else:
            for _ in range(index-1):
                prev_node = prev_node.next
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node.value
            
    def delete_all(self):
        self.tail.next = None
        self.tail = None
        self.head = None
        self.length = 0
        return "Empty"
    
new_circular_linked_list = CircularLinkedList()
new_circular_linked_list.append(5)
new_circular_linked_list.append(6)
new_circular_linked_list.append(7)
# print(new_circular_linked_list.traverse())
print(new_circular_linked_list)
new_circular_linked_list.prepend(10)
print(new_circular_linked_list)
print(new_circular_linked_list.insert(50,4))
print(new_circular_linked_list)
print(new_circular_linked_list.length)
print(new_circular_linked_list.traverse())
new_circular_linked_list.search(7)
new_circular_linked_list.get(-1)
print(new_circular_linked_list.set(3,5))
print(new_circular_linked_list)
# print(new_circular_linked_list.pop_first())
# print(new_circular_linked_list)
# print(new_circular_linked_list.pop_first())
# print(new_circular_linked_list)
# print(new_circular_linked_list.pop())
# print(new_circular_linked_list)
# print(new_circular_linked_list.pop())
# print(new_circular_linked_list)
print(new_circular_linked_list.remove(0))
print(new_circular_linked_list)
print(new_circular_linked_list.length)
# print(new_circular_linked_list.delete_all())