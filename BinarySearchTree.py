class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
def insertNode(rootNode, nodeData):
    if rootNode.data is None:
        rootNode.data = nodeData 
    elif nodeData <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeData)
        else:
            insertNode(rootNode.leftChild, nodeData)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeData)
        else:
            insertNode(rootNode.rightChild, nodeData)
    return "The Node has been successfully inserted."

def preOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        print(rootNode.data)
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        preOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        preOrderTraversal(rootNode.rightChild)
        
def postOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        postOrderTraversal(rootNode.leftChild)
        postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next
            
class Queue:
    def __init__(self):
        self.items = LinkedList()
    
    def enqueue(self,value):
        newNode = Node(value)
        if self.items.head is None:
            self.items.head = newNode
            self.items.tail = newNode
        else:
            self.items.tail.next = newNode
            self.items.tail = newNode
    
    def dequeue(self):
        if self.items.head is None:
            return 
        elif self.items.head == self.items.tail:
            removed_node = self.items.head
            self.items.head = None
            self.items.tail = None
            return removed_node
        else:
            removed_node = self.items.head
            self.items.head = self.items.head.next
            return removed_node
        
    def isEmpty(self):
        if self.items.head is None:
            return True
        else:
            return False
        
def levelOrderTraversal(rootNode):
    if rootNode is None:
        return
    else:
        custom_queue = Queue()
        custom_queue.enqueue(rootNode)
        while not custom_queue.isEmpty():
            root = custom_queue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                custom_queue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                custom_queue.enqueue(root.value.rightChild)
                
def search(rootNode, value):
    if rootNode is None:
        return
    else:
        level = 1
        custom_queue = Queue()
        custom_queue.enqueue(rootNode)
        while not custom_queue.isEmpty():
            root = custom_queue.dequeue()
            if root.value.data == value:
                return f"{value} found at level {level}."
            else:
                if root.value.leftChild is not None:
                    custom_queue.enqueue(root.value.leftChild)
                    level += 1
                
                if root.value.rightChild is not None:
                    custom_queue.enqueue(root.value.rightChild)
                
def search2(rootNode, value):
    if rootNode.data == value:
        print("Value is Found.")
    elif value < rootNode.data:
        if rootNode.leftChild.data == value:
            print("Value is Found.")
        else:
            search2(rootNode.leftChild, value)
    else:
        if rootNode.rightChild.data == value:
            print("Value is found.")
        else:
            search2(rootNode.rightChild, value)
            
def search3(rootNode, value):
    if rootNode is None:
        return ("Value not found.")
    if rootNode.data == value:
        return ("Value is Found.")
    elif value < rootNode.data:
        search2(rootNode.leftChild, value)
    else:
        search2(rootNode.rightChild, value)
                
def minValueNode(rootNode):
    current_node = rootNode
    while current_node.leftChild is not None:
        current_node = current_node.leftChild
    return current_node

def deleteNode(rootNode,value):
    if rootNode is None:
        return rootNode
    if value < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, value)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild, temp.data)
    return rootNode



def deleteBST(rootNode):
    rootNode = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    print("Successfully deleted BST.")

new_bst = BSTNode(100)
print(insertNode(new_bst, 50))    
print(insertNode(new_bst, 70))
print(insertNode(new_bst, 110))
print(insertNode(new_bst,40))
print(new_bst.rightChild.data)
print("\n")    
preOrderTraversal(new_bst)
print("\n")    
inOrderTraversal(new_bst)
print("\n")    
postOrderTraversal(new_bst)
print("\n")    
levelOrderTraversal(new_bst)
print(search(new_bst, 70))
# search2(new_bst, 70)
print(search3(new_bst, 50))
print(deleteNode(new_bst, 100).data)
print("\n")
levelOrderTraversal(new_bst)