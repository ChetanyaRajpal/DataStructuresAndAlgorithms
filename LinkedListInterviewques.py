from random import randint
class Node:
    def __init__(self, value= None):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)
    
class LinkedList:
    def __init__(self,values=None):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
    
    def __str__(self):
        values = [str(x.value) for x  in self]
        return ' -> '.join(values)
    
    def __len__(self):
        result = 0
        current_node = self.head
        while current_node:
            result += 1
            current_node = current_node.next
        return result
    
    def add(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def generate(self, n , min, max):
        self.head = None
        self.tail = None
        for _ in range(n):
            self.add(randint(min,max))
        return self
    
    def remove_duplicates(self):
        current_node = self.head
        prev_node = None
        runner = None
        while current_node:
            runner = current_node
            while runner.next:
                if runner.next.value == current_node.value:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            prev_node = current_node
            current_node = current_node.next
        self.tail = prev_node
        
    def nthToLast(self,n):
        pointer1 = self.head
        pointer2 = self.head
            
        for _ in range(n):
            if pointer2 == None:
                return None
            pointer2 = pointer2.next
            
        while pointer2:
            pointer2 = pointer2.next
            pointer1 = pointer1.next
        return pointer1
                
    def partition(self,n):
        if n < 1:
            return None
        else:
            partition_linked_list = LinkedList()
            current_node = self.head
            while current_node:
                if partition_linked_list.head is None:
                    partition_linked_list.head = current_node
                    partition_linked_list.tail = current_node
                elif current_node.value < n:
                    new_node = Node(current_node.value)
                    new_node.next = partition_linked_list.head
                    partition_linked_list.head = new_node
                else:
                    new_node = Node(current_node.value)
                    partition_linked_list.add(current_node.value)
                current_node = current_node.next
            return partition_linked_list
        
def sumLinkedList(l1,l2):
    l1_pointer = l1.head
    l2_pointer = l2.head    
    l1_string = ''
    l2_string = ''
    
    while l1_pointer:
        l1_string += str(l1_pointer.value)
        l1_pointer = l1_pointer.next
    
    while l2_pointer:
        l2_string += str(l2_pointer.value)
        l2_pointer = l2_pointer.next
    
    l1_digit = int(l1_string[::-1])
    l2_digit = int(l2_string[::-1])
    result = l1_digit + l2_digit
    result_string = str(result)
    result_string = result_string[::-1]
    result_tuple = tuple((result_string))
    new_linked_list = LinkedList()
    for i in (result_tuple):
        new_linked_list.add(int(i))
    return new_linked_list

def sum_linked_list2(l1,l2):
    n1 = l1.head
    n2 = l2.head    
    carry = 0
    ll2 = LinkedList()
    
    while n1 or n2:
        result = carry
        if n1:
            result += n1.value
            n1 = n1.next      
        if n2:
            result += n2.value
            n2 = n2.next
        ll2.add(int(result % 10))    
        carry = result / 10
    return ll2

def intersection(ll1,ll2):
    if ll1.tail.value is not ll2.tail.value:
        return False
    
    len1 = len(ll1)
    len2 = len(ll2)
    
    longer = ll1 if len1 > len2 else ll2
    shorter = ll1 if len1 < len2 else ll2
    
    diff = len(longer) - len(shorter)
    longer_node = longer.head
    shorter_node = shorter.head
    
    for _ in range(diff):
        longer_node = longer_node.next
        
    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next
        
    return longer_node.value

new_list = LinkedList()
new_list.add(4)
new_list.add(6)
new_list.add(2)
# new_list.add(5)
# new_list.add(5)
# new_list.add(6)
# new_list.add(7)
print(new_list)
# new_list.generate(10,0,100)
print(new_list)
# print(new_list.remove_duplicates())
print(len(new_list))
print(new_list)

print(new_list.nthToLast(3))
# print(new_list.partition(50))
new_list2 = LinkedList()
new_list2.add(6)
new_list2.add(6)
new_list2.add(2)
# new_list2.add(9)
# new_list2.add(7)
print(new_list2)

print(sumLinkedList(new_list,new_list2))
print(sum_linked_list2(new_list,new_list2))
print(intersection(new_list,new_list2))

