class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
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
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def get(self,index):
        temp_node = self.head
        index_count = 0
        if index <= 0:
            return None
        elif index > self.length:
            return None
        else:
            while index_count != index-1:
                temp_node = temp_node.next
                index_count += 1
            return temp_node
    
    def remove(self,index):
        index = index + 1
        if index > self.length or index <= 0:
           return None
        elif index == 1:
           temp_node = self.head
           self.head = self.head.next
           temp_node.next = None
           return temp_node.value
        elif self.length == 1:
            temp_node = self.head
            self.head = None
            self.tail = None
            return temp_node.value
        elif index == self.length:
            temp_node = self.get(index-1)
            self.tail = temp_node
            temp_node.next = None
            return temp_node.value
        else:
            prev_node = self.get(index-1)
            temp_node = prev_node.next
            prev_node.next = temp_node.next
            temp_node.next = None
            return temp_node.value
    
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
        
    def remove_duplicates(self):
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
    
    def reverse2(self,head):
        prev_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head,self.tail = self.tail, self.head
        
            
       
new_linked_list = LinkedList()
new_linked_list.append(50)
new_linked_list.append(5)
new_linked_list.append(60)
new_linked_list.append(100)
print(new_linked_list)
# print(new_linked_list.remove(0))
print(new_linked_list)
print(new_linked_list.reverse())
print(new_linked_list)
new_linked_list.append(100)
new_linked_list.append(100)
new_linked_list.append(50)
new_linked_list.append(5)
new_linked_list.append(60)
new_linked_list.append(60)
print(new_linked_list)
print(new_linked_list.length)
print(new_linked_list.remove_duplicates())
print(new_linked_list)
print(new_linked_list.tail.value)
print(new_linked_list.length)

class Solution:
    def __init__(self):
        pass
        
    def merge_linked_list(self,l1,l2):
        current_node = l1
        current_node2 = l2
        unsorted_list = []
        while current_node and current_node2:
            unsorted_list.append(current_node.value)
            unsorted_list.append(current_node2.value)
            current_node = current_node.next
            current_node2 = current_node2.next
        sorted_list = sorted(unsorted_list)
        new_linked_list3 = LinkedList()
        for i in sorted_list:
            new_linked_list3.append(i)
        print(new_linked_list3)
        
    
    def merge_linked_list2(self,l1,l2):
        current_node = l1
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = l2
        l2 = None
        temp_node = l1
        while temp_node.next:
            print(temp_node.value)
            temp_node = temp_node.next
        
new_linked_list2 = LinkedList()
new_linked_list2.append(50)
new_linked_list2.append(5)
new_linked_list2.append(60)
new_linked_list2.append(100)
print(new_linked_list)
print(new_linked_list2)

new_solution = Solution()
new_solution.merge_linked_list(new_linked_list.head, new_linked_list2.head)
print(new_solution.merge_linked_list2(new_linked_list.head, new_linked_list2.head))

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prehead = ListNode(-1)
 
        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next
 
        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2
 
        return prehead.next
    
def deleteDuplicates(head):
    current_node = head
    while current_node is not None and current_node.next is not None:
        if current_node.value == current_node.next.value:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next

def removeElements(head,val):
    dummy_head = Node(-1)
    dummy_head.next = head
    
    prev_node, current_node = dummy_head, head
    
    while current_node is not None:
        if current_node.value == val:
            prev_node.next = current_node.next
        else:
            prev_node = current_node
        current_node = current_node.next
    return dummy_head.next.value

def isPalindrome(head):
        my_list = []
        current_node = head
        while current_node:
            my_list.append(current_node.value)
            current_node = current_node.next
        if my_list == my_list[::-1]:
            return True
        return False

def isPalindrome2(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
        
    while prev:
        if head.value != prev.value:
            return False
        head = head.next
        prev = prev.next
    return True
    
new_linked_list4 = LinkedList()
new_linked_list4.append(1)
new_linked_list4.append(1)
new_linked_list4.append(3)
new_linked_list4.append(4)
new_linked_list4.append(4)
new_linked_list4.append(4)
print(new_linked_list4)

# print(deleteDuplicates(new_linked_list4.head))
# print(new_linked_list4)
# # print(removeElements(new_linked_list4.head,1))
print(new_linked_list4)
# print(new_linked_list4.head)
print(new_linked_list4.reverse2(new_linked_list4.head))
print(new_linked_list4)
print(new_linked_list)
# new_linked_list.reverse2(new_linked_list.head)
# new_linked_list.append(5)
print(new_linked_list)

new_linked_list5 = LinkedList()
new_linked_list5.append(5)
new_linked_list5.append(3)
new_linked_list5.append(3)
new_linked_list5.append(5)
print(new_linked_list5)
print(isPalindrome2(new_linked_list.head))

