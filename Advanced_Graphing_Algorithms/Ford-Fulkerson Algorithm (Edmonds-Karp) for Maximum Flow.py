from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, capacity):
        self.graph[u][v] = capacity

    # BFS to find if there is an augmenting path in the residual graph
    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()
            for v, capacity in enumerate(self.graph[u]):
                if not visited[v] and capacity > 0:  # If there is capacity and not yet visited
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True

        return False

    # Ford-Fulkerson algorithm
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V  # Store path to reconstruct it
        max_flow = 0

        while self.bfs(source, sink, parent):
            # Find the maximum flow through the path found
            path_flow = float('Inf')
            v = sink

            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.graph[u][v])
                v = u

            # Update residual capacities in the reverse direction
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = u

            max_flow += path_flow

        return max_flow

# Example usage
graph = Graph(6)
graph.add_edge(0, 1, 16)
graph.add_edge(0, 2, 13)
graph.add_edge(1, 2, 10)
graph.add_edge(1, 3, 12)
graph.add_edge(2, 1, 4)
graph.add_edge(2, 4, 14)
graph.add_edge(3, 2, 9)
graph.add_edge(3, 5, 20)
graph.add_edge(4, 3, 7)
graph.add_edge(4, 5, 4)

source = 0
sink = 5
print("The maximum possible flow is:", graph.ford_fulkerson(source, sink))
