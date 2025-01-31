#Topological Sort - Sorts given actions in such a way that if there is a dependency of one action on another, then the dependency action always comes later than its parent action.

from collections import defaultdict

class Graph:
    def __init__(self, numberOfVertices):
        self.graph = defaultdict(list)
        self.numberOfVertices = numberOfVertices
        
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)
        
    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
                
        stack.insert(0, v)
    
    def topologicalSort(self):
        visited = []
        stack = []
        
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
                
        print(stack) 
        
custom_graph = Graph(8)
custom_graph.addEdge("A", "C")
custom_graph.addEdge("C", "E")
custom_graph.addEdge("E", "H")
custom_graph.addEdge("E", "F")
custom_graph.addEdge("F", "G")
custom_graph.addEdge("B", "D")
custom_graph.addEdge("B", "C")
custom_graph.addEdge("D", "F")

custom_graph.topologicalSort()