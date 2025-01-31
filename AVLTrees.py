class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

class AVLTree:
    def __init__(self,data):
        self.rootNode = TreeNode(data)
    
    def preOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        else:
            print(rootNode.data)
            self.preOrderTraversal(rootNode.leftChild)
            self.preOrderTraversal(rootNode.rightChild)
            
    def inOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        else:
            self.inOrderTraversal(rootNode.leftChild)
            print(rootNode.data)
            self.inOrderTraversal(rootNode.rightChild)
            
    def postOrderTraversal(self, rootNode):
        if rootNode is None:
            return
        else:
            self.postOrderTraversal(rootNode.leftChild)
            self.postOrderTraversal(rootNode.rightChild)
            print(rootNode.data)
    
    def levelOrderTraversal(self,rootNode):
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
                    
            
    def search(self,rootNode, value):
        if rootNode is None:
            return "Not Found"
        elif rootNode.data == value:
            return"value Found."
        elif value < rootNode.data:
            if rootNode.leftChild.data == value:
                return "Value Found."
            return self.search(rootNode.leftChild, value)
        else:
            if rootNode.rightChild.data == value:
                return "Value Found"
            return self.search(rootNode.rightChild, value)
        
    def search2(self, root, value):
        if not root or root.data == value:
            return root
        if root.data < value:
            return self.search2(root.rightChild, value)
        return self.search2(root.leftChild, value)

    def search3(self,rootNode,value):
        if rootNode.data == value:
            return ("THe value is found.")
        elif value < rootNode.data:
            if rootNode.leftChild.data == value:
                return ("The value is found.")
            else:
                return self.search3(rootNode.leftChild, value)
        else:
            if rootNode.rightChild.data == value:
                return ("The value is found.")
            else:
                return self.search3(rootNode.rightChild, value)
            
    def search4(self, rootNode, value):
        if rootNode is None:
            return "The value is not found."
    
        if rootNode.data == value:
            return "The value is found."
        elif value < rootNode.data:
            if rootNode.leftChild is not None and rootNode.leftChild.data == value:
                return "The value is found."
            else:
                return self.search3(rootNode.leftChild, value)
        else:
            if rootNode.rightChild is not None and rootNode.rightChild.data == value:
                return "The value is found."
            else:
                return self.search3(rootNode.rightChild, value)

    def getHeight(self, rootNode):
        if not rootNode:
            return 0
        return rootNode.height
    
    def rightRotate(self, disbalancedNode):
        new_root = disbalancedNode.leftChild
        disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
        new_root.rightChild = disbalancedNode
        disbalancedNode.height = 1 + max(self.getHeight(disbalancedNode.leftChild), self.getHeight(disbalancedNode.rightChild))
        new_root.height = 1 + max(self.getHeight(new_root.leftChild), self.getHeight(new_root.rightChild))
        return new_root
    
    def leftRotate(self, disbalancedNode):
        new_root = disbalancedNode.rightChild
        disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
        new_root.leftChild = disbalancedNode
        disbalancedNode.height = 1 + max(self.getHeight(disbalancedNode.leftChild), self.getHeight(disbalancedNode.rightChild))
        new_root.height = 1 + max(self.getHeight(new_root.leftChild), self.getHeight(new_root.rightChild))
        return new_root
    
    def getBalance(self, rootNode):
        if not rootNode:
            return 0
        return self.getHeight(rootNode.leftChild) - self.getHeight(rootNode.rightChild)
    
    def insert(self, rootNode, nodeValue):
        if not rootNode:
            return TreeNode(nodeValue)
        elif nodeValue < rootNode.data:
            rootNode.leftChild = self.insert(rootNode.leftChild, nodeValue)
        else:
            rootNode.rightChild = self.insert(rootNode.rightChild, nodeValue)
            
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
        elif rootNode.data > nodeValue:
            rootNode.leftChild = self.deleteNode(rootNode.leftChild, nodeValue)
        elif rootNode.data < nodeValue:
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
    
    def deleteAVL(self, rootNode):
        rootNode.data = None
        rootNode.leftChild = None
        rootNode.rightChild = None
        return "Done."
    
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def enqueue(self,value):
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
            self.tail = None
            self.head = None
        else:
            removed_node = self.head
            self.head = self.head.next
        return removed_node

    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    
    
        
            
new_avl_tree = AVLTree(10)
new_node = TreeNode(5)
new_avl_tree.rootNode.leftChild = new_node
new_node = TreeNode(40)
new_avl_tree.rootNode.rightChild = new_node
new_node = TreeNode(70)
new_avl_tree.rootNode.rightChild.rightChild = new_node
new_avl_tree.inOrderTraversal(new_avl_tree.rootNode)
print('\n')
new_avl_tree.preOrderTraversal(new_avl_tree.rootNode)
print('\n')
new_avl_tree.postOrderTraversal(new_avl_tree.rootNode)
print('\n')
new_avl_tree.levelOrderTraversal(new_avl_tree.rootNode)
print(new_avl_tree.search(new_avl_tree.rootNode, 70))
# print(new_avl_tree.search3(new_avl_tree.rootNode,5))
# print(new_avl_tree.rootNode.leftChild.data)
print(new_avl_tree.getHeight(new_avl_tree.rootNode))
new_avl_tree.insert(new_avl_tree.rootNode, 90)
print("\n")
print(new_avl_tree.levelOrderTraversal(new_avl_tree.rootNode))
new_avl_tree.insert(new_avl_tree.rootNode, 3)
print("\n")
print(new_avl_tree.levelOrderTraversal(new_avl_tree.rootNode))
new_avl_tree.deleteNode(new_avl_tree.rootNode, 10)
print("\n")
print(new_avl_tree.levelOrderTraversal(new_avl_tree.rootNode))
new_avl_tree2 = AVLTree(100)
new_avl_tree2.rootNode = new_avl_tree2.insert(new_avl_tree2.rootNode, 51)
new_avl_tree2.rootNode = new_avl_tree2.insert(new_avl_tree2.rootNode, 151)
new_avl_tree2.rootNode = new_avl_tree2.insert(new_avl_tree2.rootNode, 1501)
new_avl_tree2.rootNode = new_avl_tree2.insert(new_avl_tree2.rootNode, 190)
new_avl_tree2.rootNode = new_avl_tree2.insert(new_avl_tree2.rootNode, 151)
print(new_avl_tree2.levelOrderTraversal(new_avl_tree2.rootNode))
