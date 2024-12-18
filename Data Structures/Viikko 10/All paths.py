class Graph:

    # Inspiration for shortest path algorith from: https://www.geeksforgeeks.org/floyd-warshall-algorithm-in-python/

    def __init__(self, n):
        self.n = n
        self.matrix = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            self.matrix[i][i] = 0

    def add(self, u, v, w):
        self.matrix[u][v] = w

    def remove(self, u, v):
        self.matrix[u][v] = float('inf')

    def all_paths(self):
        # Use Floyd-Warshall algorithm to compute shortest paths
        dist = [row[:] for row in self.matrix] 

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if dist[i][k] != float('inf') and dist[k][j] != float('inf'):
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        for i in range(self.n):
            for j in range(self.n):
                if dist[i][j] == float('inf'):
                    dist[i][j] = -1

        return dist

if __name__ == "__main__":
    graph = Graph(6)
    connections = ((0, 2, 7), (0, 4, 9), (2, 1, 5),
                   (2, 3, 1), (2, 5, 2), (3, 0, 6),
                   (3, 5, 2), (4, 5, 1), (5, 1, 6))
    for u, v, w in connections:
        graph.add(u, v, w)

    M = graph.all_paths()
    for weights in M:
        for weight in weights:
            print(f"{weight:3d}", end="")
        print()
