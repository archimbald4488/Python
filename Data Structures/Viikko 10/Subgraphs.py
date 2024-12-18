class Graph:

    # Inspiration for graph structure taken from: https://www.naukri.com/code360/library/implementation-of-graph-in-python

    def __init__(self, n):
        self.n = n
        self.vlist = {i: set() for i in range(n)}

    def add(self, u, v):
        self.vlist[u].add(v)
        self.vlist[v].add(u)

    def remove(self, u, v):
        if v in self.vlist[u]:
            self.vlist[u].remove(v)
        if u in self.vlist[v]:
            self.vlist[v].remove(u)

    def subgraphs(self):
        visited = set()
        def dfs(v):
            stack = [v]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    stack.extend(self.vlist[node] - visited)

        num_components = 0
        for vertex in range(self.n):
            if vertex not in visited:
                num_components += 1
                dfs(vertex)

        return num_components

if __name__ == "__main__":
    graph = Graph(6)

    connections = ((0, 4), (2, 1), (2, 5), (3, 0), (5, 1))
    for u, v in connections:
        graph.add(u, v)
    
    print(graph.subgraphs())
    
    more_connections = ((0, 2), (2, 3), (3, 5), (4, 5))
    for u, v in more_connections:
        graph.add(u, v)

    print(graph.subgraphs())
