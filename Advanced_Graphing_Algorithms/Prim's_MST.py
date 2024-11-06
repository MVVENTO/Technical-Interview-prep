import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]  # Adjacency list

    def add_edge(self, u, v, weight):
        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))

    def prim_mst(self):
        mst_cost = 0
        mst_edges = []
        visited = [False] * self.V
        min_heap = [(0, 0)]  # (weight, vertex)

        while min_heap:
            weight, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True
            mst_cost += weight
            mst_edges.append((u, weight))

            for next_weight, v in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (next_weight, v))

        return mst_cost, mst_edges

# Example usage
graph = Graph(4)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 6)
graph.add_edge(0, 3, 5)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 4)

mst_cost, mst_edges = graph.prim_mst()
print("Edges in MST using Prim's algorithm:")
for u, weight in mst_edges:
    print(f"Vertex: {u}, Weight: {weight}")
print(f"Total cost of MST: {mst_cost}")
