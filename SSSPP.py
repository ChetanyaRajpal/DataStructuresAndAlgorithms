#Single Source Shortest Path Problem - A single source problem is about finding a path between a given vertex (called source) to all other vertices in a graph such that the total distance between them (source and destination) is minimum.

class Graph:
    def __init__(self, gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
        
    def bfs(self, start, end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            
            for adjacent in self.gdict.get(node, []):
                new_path = list(path)
                print(new_path)
                new_path.append(adjacent)
                queue.append(new_path)
                
customDict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
               }

g = Graph(customDict)
print(g.bfs("a", "f"))