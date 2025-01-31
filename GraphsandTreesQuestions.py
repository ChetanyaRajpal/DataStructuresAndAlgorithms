class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, value):
        return self.items.append(value)
    
    def isEmpty(self):
        if self.items == []:
            return True
        return False
    
    def dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        else:
            popped_node = self.items.pop(0)
            return popped_node
        
class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    def checkRoute(self, startNode, endNode):
        queue = Queue()
        queue.enqueue(startNode)
        visited = set() 
        visited.add(startNode)
        while not queue.isEmpty():
            current_node = queue.dequeue()
            for adjacentVertex in self.gdict[current_node]:
                if adjacentVertex not in visited:
                    if adjacentVertex == endNode:
                        return True
                    else:
                        visited.add(adjacentVertex)
                        print(visited)
                        queue.enqueue(adjacentVertex)
        return False
    
customDict = { "a" : ["c","d", "b"],
            "b" : ["j"],
            "c" : ["g"],
            "d" : [],
            "e" : ["f", "a"],
            "f" : ["i"],
            "g" : ["d", "h"],
            "h" : [],
            "i" : [],
            "j" : []
               }
 
g = Graph(customDict)
print(g.checkRoute("a", "j"))
                
class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right
    
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.data
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.data
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.data
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
def minimaltree(sortedArray):
    if len(sortedArray) == 0:
        return None
    if len(sortedArray) == 1:
        return BSTNode(sortedArray[0])
    mid = int(len(sortedArray) / 2)
    left = minimaltree(sortedArray[:mid])
    right = minimaltree(sortedArray[mid+1 :])
    return BSTNode(sortedArray[mid], left, right)
    
sortedArray = [1,2,3,4,5,6,7,8,9]
bst = minimaltree(sortedArray)
bst.display()

#List of Depths
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)
            
    def __str__(self):
        return "({val})".format(val = self.val) + str(self.next)
    
class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def depth(tree):
    if tree == None:
        return 0
    if tree.left == None and tree.right == None:
        return 1
    
    else:
        depthLeft = 1 + depth(tree.left)
        depthRight = 1 + depth(tree.right)
        if depthLeft > depthRight:
            return depthLeft
        else:
            return depthRight
        
def treeToLinkedList(tree, custDict = {}, d = None):
    if d == None:
        d = depth(tree)
    if custDict.get(d) == None:
        custDict[d] = LinkedList(tree.val)
    else:
        custDict[d].add(tree.val)
        if d == 1:
            return custDict
    if tree.left != None:
        custDict = treeToLinkedList(tree.left, custDict, d-1)
    if tree.right != None:
        custDict = treeToLinkedList(tree.right, custDict, d-1)
    return custDict

mainTree = BinaryTree(1)
two = BinaryTree(2)
three = BinaryTree(3)
four = BinaryTree(4)
five = BinaryTree(5)
six = BinaryTree(6)
seven = BinaryTree(7)
mainTree.left = two
mainTree.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

custDict = treeToLinkedList(mainTree)
for depthLevel, LinkedList in custDict.items():
    print("{0} {1}".format(depthLevel, LinkedList))
    

         