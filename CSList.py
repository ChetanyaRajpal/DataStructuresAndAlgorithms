class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return str(self.value)

class CSLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += '=>'
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1
        
    def delete_by_value(self, value):
        pre_node = self.head
        popped_node = None
        if self.length == 0:
            return False
        elif self.head.value == value:
            popped_node = self.head
            self.head = popped_node.next
            self.tail.next = self.head
            popped_node.next = None
            
        elif self.tail.value == value:
            popped_node = self.tail
            pre_node = self.head
            for _ in range(self.length-2):
                pre_node = pre_node.next
            pre_node.next = popped_node.next
            self.tail = pre_node
            self.tail.next = self.head
            popped_node.next = None
                
        else:
            for _ in range(self.length - 1):
                if pre_node.next.value == value:
                    popped_node = pre_node.next
                    pre_node.next = popped_node.next
                    popped_node.next = None
                else:
                    pre_node = pre_node.next
                    if pre_node == self.head:
                        break
        self.length -= 1
        return popped_node.value

    def count_nodes(self):
        count = 1
        temp_node = self.head
        while temp_node:
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            count += 1
        return count
    
    def split_list(self):
        if self.length == 0:
            return None, None
        list_1 = ''
        list_2 = ''
        temp_node = self.head
        range_val = 0
        index_val = 1
        if self.length%2 == 0:
            range_val = (self.length/2) + 1
            for _ in range(1,int(range_val)):
                list_1 += str(temp_node.value)
                index_val += 1
                temp_node = temp_node.next
                if index_val == range_val:
                    break
                list_1 += ' -> '
                
            for _ in range(int(range_val),self.length+1):
                list_2 += str(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.head:
                    break
                list_2 += ' -> '
        else:
            range_val = (self.length+1)/2
            for _ in range(1,int(range_val+1)):
                list_1 += str(temp_node.value)
                index_val += 1
                temp_node = temp_node.next
                if index_val == range_val+1:
                    break
                list_1 += ' -> '
                
            for _ in range(int(range_val),self.length+1):
                list_2 += str(temp_node.value)
                temp_node = temp_node.next
                if temp_node == self.head:
                    break
                list_2 += ' -> '
        return list_1,list_2
    
    def split_list2(self):
        if self.length == 0:
            return None, None
 
        mid = (self.length + 1) // 2
        count = 1
 
        first_list = CSLinkedList()
        second_list = CSLinkedList()
 
        current = self.head
        last_first_list = None
 
        while count <= mid:
            first_list.append(current.value)
            last_first_list = current
            current = current.next
            count += 1
 
        # Set the tail of the first half
        if last_first_list:
            first_list.tail = last_first_list
            first_list.tail.next = first_list.head
 
        # Handle the second half
        while current != self.head:
            second_list.append(current.value)
            current = current.next
 
        # Set the tail of the second half
        if second_list.length > 0:
            second_list.tail = self.tail
            second_list.tail.next = second_list.head
 
        print(first_list, second_list)
        
    def is_sorted(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return None
        temp_node = self.head
        next_node = self.head.next
        while next_node and temp_node:
            if temp_node.value > next_node.value:
                return False
            next_node = next_node.next
            temp_node = next_node
            if next_node == self.head:
                break
            return True
    
    def is_sorted2(self):
        if self.head is None:
            return True  # An empty list is considered sorted.
        
        temp = self.head
        while temp.next != self.head:
            if temp.data > temp.next.data:
                return False
            temp = temp.next
 
        return True
    
    def insert_into_sorted(self,value):
        if self.head == None:
            self.prepend(value)
        elif value <= self.head.value:
            self.prepend(value)
        elif value > self.tail.value:
            self.append(value)
        else:
            new_node = Node(value)
            temp_node = self.head
            while temp_node:
                if temp_node.next.value >= new_node.value:
                    new_node.next = temp_node.next
                    temp_node.next = new_node
                    break
                temp_node = temp_node.next
                if temp_node == self.head:
                    break
            self.length += 1
            
    def josephus_circle(self,step):
        temp = self.head
        while self.length > 1:
            count = 1
            while count != step:
                temp = temp.next
                count += 1
            print(f"Removed Node : {temp.value}")
            deleted_node = temp
            temp = temp.next
            self.delete_by_value(deleted_node.value) 
        return f"last person standing {temp.value}"
    
    def josephus_circle2(self, step):
        temp = self.head
 
        while self.count_nodes() > 1:
            count = 1
            while count != step:
                temp = temp.next
                count += 1
            print(f"Removed: {temp.value}")
            self.delete_by_value(temp.value)
            temp = temp.next
 
        return f"Last person left standing: {temp.value}"

new_linkedlist = CSLinkedList()
new_linkedlist.append(10)
new_linkedlist.append(50)
new_linkedlist.prepend(100)
print(new_linkedlist)
print(new_linkedlist.delete_by_value(50))
print(new_linkedlist.tail.next.value)
print(new_linkedlist)
print(new_linkedlist.length)
print(new_linkedlist.count_nodes())
new_linkedlist.append(60)
new_linkedlist.append(70)
new_linkedlist.append(50)
# new_linkedlist.append(90)
print(new_linkedlist)

print(new_linkedlist.split_list())
print(new_linkedlist.split_list2())
print(new_linkedlist.is_sorted())

sorted_circular_linked_list = CSLinkedList()
sorted_circular_linked_list.append(5)
sorted_circular_linked_list.append(10)
sorted_circular_linked_list.append(15)
sorted_circular_linked_list.append(20)
sorted_circular_linked_list.append(25)
sorted_circular_linked_list.append(30)
print(sorted_circular_linked_list)
print(sorted_circular_linked_list.is_sorted())
print(sorted_circular_linked_list.prepend(4))
sorted_circular_linked_list.insert_into_sorted(35)

print(sorted_circular_linked_list.head.value)
print(sorted_circular_linked_list)
print(sorted_circular_linked_list.length)
print(sorted_circular_linked_list.josephus_circle(2))