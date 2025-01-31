# Vertices - Vertices are the nodes of the graph.
# Edge - The edge is the line that connects pair of vertices.
# Unweighted graph - A graph which doesnot have any weighted edge.
# Weighted graph - A graph which has a weight associated with any edge.
# Undirected graph - In case the edges of the graph do not have a direction associated with them. 
# Directed graph - If the edges in the graph have a direction associated with them.
# Cyclic graph - A graph which has at least one loop.
# Acyclic graph - A graph with no loop.
# Tree - It is a special case of directed acyclic graphs.

# Types of Graphs
# Unweighted - Undirected Graph
# Unweighted - Directed Graph
# Positive - Weighted - Undirected Graph
# Positive - Weighted - Directed Graph
# Negative - Weighted - Undirected Graph
# Negative - Weighted - Directed Graph

# Adjacecy Matrix - An adjacency matrix is a square matrix or you can say it is a 2D array and the elements of the matrix indicated whether pairs of vertices are adjacent or not in the graph. 
# Adjacency List - An adjacency list is a collection of unordered list used to represent a graph. Each list describes the set of neighbors of a vertex in the group.

# If a graph is complete or almost complete, we should use Adjacency Matrix.
# If the number of edges are few then we should use Adjacency List.


class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
        
    def add_vertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False
    
    def __str__(self):
        stri = ""
        for vertex in self.gdict:
            stri += vertex
            stri += " : "
            stri += str(self.gdict[vertex])
            stri += "\n"
        return stri
    
    def print_graph(self):
        for vertex in self.gdict:
            print(vertex, " : ", self.gdict[vertex])
            
    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False
    
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].remove(vertex2)
            self.gdict[vertex2].remove(vertex1)
            return True
        return False
    
    def removeVertex(self, vertex):
        if vertex in self.gdict.keys():
            for i in self.gdict[vertex]:
                self.gdict[i].remove(vertex)
            del self.gdict[vertex]
            return True
        return False
    
    def breadthFirstSearch(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = [vertex]
        while queue:
            current_vertex = queue.pop(0)
            print(current_vertex)
            for adjacent_vertex in self.gdict[current_vertex]:
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex)
                    
    def depthFirstSearch(self, vertex):
        visited = set()
        stack = [vertex]
        while stack:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                visited.add(current_vertex)
                print(current_vertex)
            for i in self.gdict[current_vertex]:
                if i not in visited:
                    stack.append(i)
        
        
customDict = {"a" : ["b", "c"],
              "b" : ["a", "d"],
              "c" : ["a", "e"],
              "d" : ["b" , "e", "f"],
              "e" : ["d", "f", "c"],
              "f" : ["d", "e"] 
              }

graph = Graph(customDict)
print(graph.gdict)
graph.addEdge("e" , "a")
print(graph.gdict["e"])

print(graph)
graph.print_graph()

print(graph.removeEdge("e", "a"))
print(graph)

graph2 = Graph()
graph2.add_vertex("A")
graph2.add_vertex("B")
graph2.add_vertex("C")
print(graph2)

graph2.addEdge("A", "C")
graph2.addEdge("A", "B")
graph2.addEdge("C", "B")
print(graph2)

graph2.removeEdge("A", "C")
print(graph2)

graph2.removeVertex("C")
print(graph2)

graph.breadthFirstSearch("a")
print("\n")
graph.depthFirstSearch("a")