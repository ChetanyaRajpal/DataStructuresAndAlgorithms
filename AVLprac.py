class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

class AVLTree:
    def __init__(self, data):
        self.rootNode = TreeNode(data)
    
    def preOrderTraversal(self, rootNode):
        if not rootNode:
            return
        print(rootNode.data)
        self.preOrderTraversal(rootNode.leftChild)
        self.preOrderTraversal(rootNode.rightChild)
        
    def inOrderTraversal(self, rootNode):
        if not rootNode:
            return
        self.inOrderTraversal(rootNode.leftChild)
        print(rootNode.data)
        self.inOrderTraversal(rootNode.rightChild)
    
    def postOrderTraversal(self, rootNode):
        if not rootNode:
            return
        self.postOrderTraversal(rootNode.leftChild)
        self.postOrderTraversal(rootNode.rightChild)
        print(rootNode.data)
        
    def levelOrderTraversal(self, rootNode):
        if not rootNode:
            return 
        else:
            custom_queue = Queue()
            custom_queue.enqueue(rootNode)
            while not custom_queue.isEmpty():
                root = custom_queue.dequeue()
                print(root.value.data)
                if root.value.leftChild is not None:
                    custom_queue.enqueue(root.value.leftChild)
                if root.value.rightChild  is not None:
                    custom_queue.enqueue(root.value.rightChild)
                    
    def search(self, rootNode, nodeValue):
        if not rootNode:
            return None
        elif rootNode.data == nodeValue:
            return "Value Found!"
        elif nodeValue < rootNode.data:
            return self.search(rootNode.leftChild, nodeValue)
        elif nodeValue > rootNode.data:
            return self.search(rootNode.rightChild, nodeValue)
        else:
            return "Not Found!"
        
    def getHeight(self, rootNode):
        if not rootNode:
            return 0
        else:
            return rootNode.height
        
    def leftRotate(self, rootNode):
        new_root = rootNode.rightChild
        rootNode.rightChild = rootNode.rightChild.leftChild
        new_root.leftChild = rootNode
        rootNode.height = 1 + max(self.getHeight(rootNode.leftChild), self.getHeight(rootNode.rightChild))
        new_root.height = 1 + max(self.getHeight(new_root.leftChild), self.getHeight(new_root.rightChild))
        return new_root
        
    def rightRotate(self, rootNode):
        new_root = rootNode.leftChild
        rootNode.leftChild = rootNode.leftChild.rightChild
        new_root.rightChild = rootNode
        rootNode.height = 1 + max(self.getHeight(rootNode.leftChild), self.getHeight(rootNode.rightChild))
        new_root.height = 1 + max(self.getHeight(new_root.leftChild), self.getHeight(new_root.rightChild))
        return new_root
    
    def getBalance(self, rootNode):
        if rootNode is None:
            return 0
        else: 
            return self.getHeight(rootNode.leftChild) - self.getHeight(rootNode.rightChild)
        
    def insert(self, rootNode, nodeValue):
        if not rootNode:
            return TreeNode(nodeValue)
        elif nodeValue > rootNode.data:
            rootNode.rightChild = self.insert(rootNode.rightChild, nodeValue)
        else:
            rootNode.leftChild = self.insert(rootNode.leftChild, nodeValue)
        rootNode.height = 1 + max(self.getHeight(rootNode.leftChild), self.getHeight(rootNode.rightChild))
        balance = self.getBalance(rootNode)
        if balance > 1 and nodeValue < rootNode.leftChild.data:
            return self.rightRotate(rootNode)
        if balance > 1 and nodeValue > rootNode.leftChild.data:
            rootNode.leftChild = self.leftRotate(rootNode.leftChild)
            return self.rightRotate(rootNode)
        if balance < -1 and nodeValue > rootNode.rightChild.data:
            return self.leftRotate(rootNode)
        if balance < -1 and nodeValue < rootNode.rightChild.data:
            rootNode.rightChild = self.rightRotate(rootNode.rightChild)
            return self.leftRotate(rootNode)
        return rootNode
    
    def getMinimum(self, rootNode):
        if rootNode is None or rootNode.leftChild is None:
            return rootNode
        return self.getMinimum(rootNode.leftChild)
        
    def deleteNode(self, rootNode, nodeValue):
        if not rootNode:
            return rootNode
        elif nodeValue < rootNode.data:
            rootNode.leftChild = self.deleteNode(rootNode.leftChild, nodeValue)
        elif nodeValue > rootNode.data:
            rootNode.rightChild = self.deleteNode(rootNode.rightChild, nodeValue)
        else:
            if rootNode.leftChild is None:
                temp = rootNode.rightChild
                rootNode = None
                return temp
            elif rootNode.rightChild is None:
                temp = rootNode.leftChild
                rootNode = None
                return temp
            temp = self.getMinimum(rootNode.rightChild)
            rootNode.data = temp.data
            rootNode.rightChild = self.deleteNode(rootNode.rightChild, temp.data)
        rootNode.height = 1 + max(self.getHeight(rootNode.leftChild), self.getHeight(rootNode.rightChild))
        balance = self.getBalance(rootNode)
        if balance > 1 and self.getBalance(rootNode.leftChild) >= 0:
            return self.rightRotate(rootNode)
        if balance < -1 and self.getBalance(rootNode.rightChild) <= 0:
            return self.leftRotate(rootNode)
        if balance > 1 and self.getBalance(rootNode.leftChild) < 0:
            rootNode.leftChild = self.leftRotate(rootNode.leftChild)
            return self.rightRotate(rootNode)
        if balance < -1 and self.getBalance(rootNode.rightChild) > 0:
            rootNode.rightChild = self.rightRotate(rootNode.rightChild)
            return self.leftRotate(rootNode)
        return rootNode
            


        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
    def dequeue(self):
        if self.head is None:
            return None
        elif self.head == self.tail:
            removed_node = self.head
            self.head = None
            self.tail = None
        else:
            removed_node = self.head
            self.head = self.head.next
        return removed_node
    
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False


def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insertNode(rootNode, nodeValue):
    if not rootNode:
        return TreeNode(nodeValue)
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode


    
# new_avl_tree = AVLTree(5)
# new_avl_tree.insert(new_avl_tree.rootNode, 3)
# new_avl_tree.insert(new_avl_tree.rootNode, 7)
# print(new_avl_tree.rootNode.leftChild.data)
# print(new_avl_tree.rootNode.rightChild.data)
# new_avl_tree.insert(new_avl_tree.rootNode, 17)
# new_avl_tree.insert(new_avl_tree.rootNode,40)

# print(new_avl_tree.rootNode.data)
# new_avl_tree.insert(new_avl_tree.rootNode, 3)
# new_avl_tree.insert(new_avl_tree.rootNode, 7)
# print('\n')
# new_avl_tree.levelOrderTraversal(new_avl_tree.rootNode)
new_avl_tree2 = AVLTree(100)
new_avl_tree2.rootNode = insertNode(new_avl_tree2.rootNode, 1900)
new_avl_tree2.rootNode = insertNode(new_avl_tree2.rootNode, 100)
new_avl_tree2.rootNode = insertNode(new_avl_tree2.rootNode, 1160)
new_avl_tree2.rootNode = insertNode(new_avl_tree2.rootNode, 90)
print('\n')
new_avl_tree2.levelOrderTraversal(new_avl_tree2.rootNode)
new_avl_tree2.rootNode = new_avl_tree2.deleteNode(new_avl_tree2.rootNode, 100)
print('\n')
new_avl_tree2.levelOrderTraversal(new_avl_tree2.rootNode)