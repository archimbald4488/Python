import heapq

class Graph:

    # Inspiration for Kruskal's algorithm taken from: https://www.geeksforgeeks.org/kruskals-algorithm-in-python/

    def __init__(self, n):
        self.n = n
        self.edges = []  # List to store all edges in the form (weight, u, v)

    def add(self, u, v, w):
        self.edges.append((w, u, v))

    def remove(self, u, v):
        self.edges = [(w, x, y) for (w, x, y) in self.edges if not (x == u and y == v or x == v and y == u)]

    def min_cost(self):
        # Use Kruskal's algorithm to find MST
        parent = list(range(self.n))
        rank = [0] * self.n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1

        self.edges.sort()
        total_cost = 0
        mst_edges = 0

        for w, u, v in self.edges:
            if find(u) != find(v):
                union(u, v)
                total_cost += w
                mst_edges += 1
                if mst_edges == self.n - 1:
                    break

        # if not enough edges return 0
        return total_cost if mst_edges == self.n - 1 else 0

if __name__ == "__main__":
    graph = Graph(6)
    connections = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
                   (2, 3, 1), (2, 5, 2), (3, 0, 6),
                   (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in connections:
        graph.add(u, v, w)

    print(graph.min_cost())

    graph.remove(2, 3)

    print(graph.min_cost())
