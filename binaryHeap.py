class Heap:
    def __init__(self, size):
        self.custom_list = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1
        
    def peekOfHeap(self, rootNode):
        if  not rootNode:
            return
        else:
            return rootNode.custom_list[1]
        
    def sizeOfHeap(self, rootNode):
        if not rootNode:
            return
        else:
            return rootNode.heapSize
        
    def levelOrderTraversal(self, rootNode):
        if not rootNode:
            return
        for i in range(1,rootNode.heapSize + 1):
            print(rootNode.custom_list[i])
            
    def heapifyTreeInsert(self, rootNode, index, heapType):
        parent_index = int(index/2)
        if index <= 1:
            return
        if heapType == "min":
            if rootNode.custom_list[index] < rootNode.custom_list[parent_index]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[parent_index]
                rootNode.custom_list[parent_index] = temp
            self.heapifyTreeInsert(rootNode, parent_index, heapType)
        elif heapType == "max":
            if rootNode.custom_list[index] > rootNode.custom_list[parent_index]:
                temp = rootNode.custom_list[index]
                rootNode.custom_list[index] = rootNode.custom_list[parent_index]
                rootNode.custom_list[parent_index] = temp
            self.heapifyTreeInsert(rootNode, parent_index, heapType)
            
    def insertNode(self, rootNode, nodeValue, heapType):
        if rootNode.heapSize + 1 == rootNode.maxSize:
            return "The Binary Heap is Full."
        rootNode.custom_list[rootNode.heapSize + 1 ] = nodeValue
        rootNode.heapSize += 1
        self.heapifyTreeInsert(rootNode, rootNode.heapSize, heapType)
        return "The node has been successfully inserted."
    
    def heapifyTreeExtract(self, rootNode, index, heapType):
        leftIndex = index * 2
        rightIndex = index * 2 + 1
        swapChild = 0
        
        if rootNode.heapSize < leftIndex:
            return
        elif rootNode.heapSize == leftIndex:
            if heapType == "min":
                if rootNode.custom_list[index] > rootNode.custom_list[leftIndex]:
                    temp = rootNode.custom_list[index]
                    rootNode.custom_list[index] = rootNode.custom_list[leftIndex]
                    rootNode.custom_list[leftIndex] = temp
                return
            else:
                if rootNode.custom[index] < rootNode.custom_list[leftIndex]:
                    temp = rootNode.custom_list[index]
                    rootNode.custom_list[index] = rootNode.custom_list[leftIndex]
                    rootNode.custom_list[leftIndex] = temp
                return
        else:
            if heapType == "min":
                if rootNode.custom_list[leftIndex] < rootNode.custom_list[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if rootNode.custom_list[index] > rootNode.custom_list[swapChild]:
                    temp = rootNode.custom_list[index]
                    rootNode.custom_list[index] = rootNode.custom_list[swapChild]
                    rootNode.custom_list[swapChild] = temp
            else:
                if rootNode.custom_list[leftIndex] > rootNode.custom_list[rightIndex]:
                    swapChild = leftIndex
                else:
                    swapChild = rightIndex
                if rootNode.custom_list[index] < rootNode.custom_list[swapChild]:
                    temp = rootNode.custom_list[index]
                    rootNode.custom_list[index] = rootNode.custom_list[swapChild]
                    rootNode.custom_list[swapChild] = temp
                
            self.heapifyTreeExtract(rootNode, swapChild, heapType)
            
    def extract(self, rootNode, heapType):
        if rootNode.heapSize == 0:
            return
        else:
            extractedNode = rootNode.custom_list[1]
            rootNode.custom_list[1] = rootNode.custom_list[rootNode.heapSize]
            rootNode.custom_list[rootNode.heapSize] = None
            rootNode.heapSize -= 1
            self.heapifyTreeExtract(rootNode, 1, heapType)
            return extractedNode
        
    def deleteEntireBP(self, rootNode):
        rootNode.custom_list = None
                
    
new_heap = Heap(5)
new_heap.insertNode(new_heap, 4, "max")
new_heap.insertNode(new_heap, 5, "max")
new_heap.insertNode(new_heap, 2, "max")
new_heap.insertNode(new_heap, 1, "max")

new_heap.levelOrderTraversal(new_heap)
print(new_heap.extract(new_heap, "max"))
print('\n')
new_heap.insertNode(new_heap, 5, "max")
new_heap.levelOrderTraversal(new_heap)
