#Linked List is a form of sequential collection and it doesnt have to be in order. A Linked List is made up of independent nodes that may contain any type of data and each node has a reference to the next node in the link.
#Linked List with one node

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    #Creating a method that will print the linked list in the console.
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result
          
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def insert(self,value,index):
        new_node = Node(value)
        if index == 1:
            self.prepend(value)
        elif index <= 0:
            self.append(value)
        elif self.length == 0:
            self.head = new_node
            self.tail = new_node
        elif index > self.length:
            self.append(value)
        else:
            temp_node = self.head
            for i in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
            self.length += 1
        return True
    
    def traversal(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
    
    def search(self,value_to_search):
        temp_node = self.head
        index = 0
        while temp_node is not None:
            if temp_node.value == value_to_search:
                return (f"found at {index}")
            temp_node = temp_node.next
            index += 1
        return False

    def get(self,index):
        temp_node = self.head
        index_count = 0
        if index <= 0:
            return False
        elif index > self.length:
            return False
        else:
            while index_count != index-1:
                temp_node = temp_node.next
                index_count += 1
            return temp_node
    
    def set(self,index,value):
        temp_node = self.head
        if index <= 0:
            return False
        elif index > self.length:
            return False
        else:
            if temp_node:
                for _ in range(index-1):
                    temp_node = temp_node.next
                temp_node.value = value
                return value
        
    def pop_first(self):
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node.value
        elif self.length == 0:
            return False
        else:
            self.head = self.head.next
            popped_node.next = None
            self.length -= 1
            return popped_node.value
        
    def pop(self):
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node.value
        elif self.length == 0:
            return False
        else:
            temp_node = self.head
            for _ in range(self.length-2):
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
            self.length -= 1
            return popped_node.value
        
    def remove(self,index):
        prev_node = self.get(index-1)
        if index <= 0:
            return False
        elif index > self.length:
            return False
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        elif index == 1:
            self.pop_first()
        elif index == self.length:
            self.pop()
        else:
            temp_node = prev_node.next
            prev_node.next = temp_node.next
            temp_node.next = None
            self.length -= 1
            return temp_node.value
        
    def remove_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        return "cleared all"
    
    def reverse(self):
        prev_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
            print(prev_node.value)
        self.head,self.tail = self.tail,self.head
        
    def find_middle(self):
        index = 1
        temp_node = self.head
        if self.length%2 == 0:
            while index != self.length/2 + 1:
                temp_node = temp_node.next
                index += 1
                print(temp_node.value)
        else:
            while index != (self.length + 1)/2:
                temp_node = temp_node.next
                index += 1
                print(temp_node.value)
                
    def find_middle2(self):
        slow = self.head
        fast = self.head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value
    
    def remove_duplicates(self):
        if self.head is None:
            return
        node_values = set()  # set to store unique node values
        current_node = self.head
        node_values.add(current_node.value)
        while current_node.next:
            if current_node.next.value in node_values:  # duplicate found
                current_node.next = current_node.next.next
                self.length -= 1
            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next
        self.tail = current_node
        
    def remove_duplicates2(self):
        my_set = set()
        current_node = self.head
        pre_node = None
        for _ in range(self.length):
            if current_node.value in my_set:
                next_node = current_node.next
                pre_node.next = current_node.next
                current_node.next = None
                current_node = next_node
                self.tail = pre_node
                self.length -= 1
            else:
                my_set.add(current_node.value)
                next_node = current_node.next
                pre_node = current_node
                current_node = next_node
                self.tail = current_node
        return my_set
    

new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.prepend(30)
print(new_linked_list.head.value)
print(new_linked_list.tail.value)
print(new_linked_list.length)
print(new_linked_list)
new_linked_list.insert(50,5)
print(new_linked_list)
print(new_linked_list.length)
new_linked_list.traversal()
print(new_linked_list.search(10))
print(new_linked_list.get(4))
print(new_linked_list.set(4,100))
print(new_linked_list)
# print(new_linked_list.pop_first())
print(new_linked_list)
# print(new_linked_list.pop())
print(new_linked_list)
print(new_linked_list.tail.value)
print(new_linked_list.remove(4))
print(new_linked_list)
print(new_linked_list.length)
print(new_linked_list.tail.value)
print(new_linked_list.reverse())
print(new_linked_list)
new_linked_list.append(50)
print(new_linked_list)
new_linked_list.find_middle()
print(new_linked_list.find_middle2())
new_linked_list.append(20)
print(new_linked_list)
new_linked_list.remove_duplicates()
print(new_linked_list)