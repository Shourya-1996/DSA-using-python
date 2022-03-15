class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            dequeueVertex = queue.pop(0)
            print(dequeueVertex)
            for adjacentVertex in self.gdict[dequeueVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)


custdict = {"a": ["b", "c"],
            "b": ["a", "b", "e"],
            "c": ["b", "e"],
            "d": ["b", "e", "f"],
            "e": ["d", "f"],
            "f": ["d", "e"]
            }

graph = Graph(custdict)
# print(graph.gdict)
# graph.addEdge("e", "c")
# print(graph.gdict["e"])
# graph.bfs("a")
graph.dfs("a")
