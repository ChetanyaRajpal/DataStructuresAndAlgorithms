class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
        
    def __str__(self,level=0):
        ret = "  " * level + str(self.data) + "\n"
        for child in self.children:
            ret+= child.__str__(level + 1)
        return ret
    
    def addChild(self,TreeNode):
        self.children.append(TreeNode)
        
tree = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
cola = TreeNode("Cola", [])
fanta = TreeNode("Fanta", [])

tree.addChild(cold)
tree.addChild(hot)
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(cola)
cold.addChild(fanta)

print(tree)

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None 
        
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild
leftChild.leftChild = TreeNode("Tea")
leftChild.rightChild = TreeNode("Coffee")

def preOrderTraversal(rootNode):
    if not rootNode:
        return 
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    
preOrderTraversal(newBT)
print("\n")

def inOrderTraversal(rootNode):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)
    
inOrderTraversal(newBT)
print("\n")

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)
    
postOrderTraversal(newBT)
print("\n")

class Node:
    def __init__(self,value):
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
        
    def __str__(self):
        result = ''
        current_node = self.items.head
        while current_node:
            result += str(current_node.value)
            if current_node.next:
                result += " -> "
            current_node = current_node.next
    
    def enqueue(self,value):
        new_node = Node(value)
        if self.items.head is None:
            self.items.head = new_node
            self.items.tail = new_node
        else:
            self.items.tail.next = new_node
            self.items.tail = new_node
        
    def dequeue(self):
        if self.items.head is None:
            return None
        else:
            if self.items.head == self.items.tail:
                removed_node = self.items.head
                self.items.head = None
                self.items.tail = None
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
    if not rootNode:
        return 
    else:
        customqueue = Queue()
        customqueue.enqueue(rootNode)
        while not customqueue.isEmpty():
            root = customqueue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                customqueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customqueue.enqueue(root.value.rightChild)
                
levelOrderTraversal(newBT)
print("\n")

def search(rootNode, value):
    if not rootNode:
        return "The tree is Empty"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.data == value:
                return True
            if (root.value.leftChild is not None):
                customQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                customQueue.enqueue(root.value.rightChild)
            
        return False
            
print(search(newBT, "Hot"))

def insert(rootNode,value):
    new_node = TreeNode(value)
    if not rootNode:
        rootNode = new_node
    else:
        custom_queue = Queue()
        custom_queue.enqueue(rootNode)
        while not custom_queue.isEmpty():
            root = custom_queue.dequeue()
            if root.value.leftChild is not None:
                custom_queue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = new_node
                return "Done"
            
            if root.value.rightChild is not None:
                custom_queue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = new_node
                return "Done"
                
print(insert(newBT, "Soda"))
print(insert(newBT, "Milkshakes"))
print(insert(newBT, "Green Tea"))
print(insert(newBT, "Hot Tea"))
print(levelOrderTraversal(newBT))

def getDeepestNode(rootNode):
    if not rootNode:
        return "The tree is Empty"
    else:
        custom_queue = Queue()
        custom_queue.enqueue(rootNode)
        while not custom_queue.isEmpty():
            root = custom_queue.dequeue()
            if root.value.leftChild is not None:
                custom_queue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                custom_queue.enqueue(root.value.rightChild)
        deepest_node = root.value
        return deepest_node
    
print(getDeepestNode(newBT).data)

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return "The Tree is Empty"
    else:
        customQueue = Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    customQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    customQueue.enqueue(root.value.leftChild)
                        
def deleteNode(rootNode, node):
    if not rootNode:
        return "The tree is empty."
    else:
        custom_queue = Queue()
        custom_queue.enqueue(rootNode)
        while  not custom_queue.isEmpty():
            root = custom_queue.dequeue()
            if root.value.data == node:
                deepest_node = getDeepestNode(rootNode)
                print(f"THe deepest Node : {deepest_node.data}")
                root.value.data = deepest_node.data
                deleteDeepestNode(rootNode, deepest_node)
                return "The Node has been successfully deleted."
            if root.value.leftChild is not None:
                custom_queue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                custom_queue.enqueue(root.value.rightChild)
        return "Node Doesn't Exist."
    
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The BT has been successfully deleted."

deepest_node = getDeepestNode(newBT)
deleteDeepestNode(newBT,deepest_node)
print("\n")
print(levelOrderTraversal(newBT))

print(deleteNode(newBT, "Soda"))
print("\n")
print(levelOrderTraversal(newBT))
print(deleteNode(newBT, "Tea"))
print("\n")
print(levelOrderTraversal(newBT))

class BinaryTree:
    def __init__(self,size):
        self.custom_list = size * [None]
        self.maxSize = size
        self.lastUsedIndex = 0
        
    def insert(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            return "The Tree is Full."
        else:
            self.custom_list[self.lastUsedIndex+1] = value
            self.lastUsedIndex += 1
            return "Successfully Inserted."
        
    def search(self,value):
        for i in self.custom_list:
            if i == value:
                return "Success"
        return "Not Found"
    
    def preOrderTraversal(self, index=1):
        if index > self.lastUsedIndex:
            return
        print(self.custom_list[index])
        self.preOrderTraversal(2 * index)
        self.preOrderTraversal(2 * index + 1)
        
    def inOrderTraversal(self,index=1):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(2 * index)
        print(self.custom_list[index])
        self.inOrderTraversal(2 * index + 1)
        
    def postOrderTraversal(self,index=1):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.custom_list[index])
                
    def levelOrderTraversal(self,index=1):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.custom_list[i])
    
    def deleteNode(self, node):
        if self.lastUsedIndex == 0:
            return "The tree is Empty."
        for i in range(1, self.lastUsedIndex + 1):
            if self.custom_list[i] == node:
                self.custom_list[i] = self.custom_list[self.lastUsedIndex]
                self.custom_list[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The Node has been successfully deleted."
            
    def deleteBT(self):
        self.custom_list = None
        self.lastUsedIndex = 0
        return "The BT has been successfull deleted"
    
new_BT = BinaryTree(8)
new_BT.insert("Drinks")
new_BT.insert("Hot")
new_BT.insert("Cold")
new_BT.insert("Tea")
new_BT.insert("Coffee")
new_BT.insert("Soda")

print(new_BT.custom_list)
print(new_BT.search("Water"))
new_BT.preOrderTraversal()
print("\n")
new_BT.inOrderTraversal()
print("\n")
new_BT.postOrderTraversal()
print("\n")
new_BT.levelOrderTraversal()
# new_BT.deleteNode("Hot")
new_BT.levelOrderTraversal()


