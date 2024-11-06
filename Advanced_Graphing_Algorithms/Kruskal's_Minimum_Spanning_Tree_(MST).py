class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []  # List to store graph edges

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    # Helper function to find set of an element (uses path compression)
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Helper function to unite two subsets
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Kruskal's algorithm to find MST
    def kruskal_mst(self):
        self.edges = sorted(self.edges)  # Sort edges by weight
        parent, rank = [], []
        mst = []  # Store the resulting MST edges

        # Initialize subsets for each vertex
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        for weight, u, v in self.edges:
            # Find the root of the sets of u and v
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            # Only add the edge if it doesn’t form a cycle
            if root_u != root_v:
                mst.append((u, v, weight))
                self.union(parent, rank, root_u, root_v)

        # Print or return the MST
        return mst

# Example usage
graph = Graph(4)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 6)
graph.add_edge(0, 3, 5)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 4)

mst = graph.kruskal_mst()
print("Edges in MST using Kruskal's algorithm:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
