# 1. Graph Representations
# Adjacency Matrix:

# python
# Copy code
# Example of an adjacency matrix representation for a graph with 4 vertices
# Adjacency Matrix for a directed graph
#     0  1  2  3
# 0 [ 0, 1, 0, 0 ]
# 1 [ 0, 0, 1, 1 ]
# 2 [ 1, 0, 0, 1 ]
# 3 [ 0, 0, 0, 0 ]

def create_adj_matrix(num_vertices, edges):
    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for u, v in edges:
        adj_matrix[u][v] = 1
    return adj_matrix

num_vertices = 4
edges = [(0, 1), (1, 2), (1, 3), (2, 0), (2, 3)]
print(create_adj_matrix(num_vertices, edges))
Adjacency List:

# python
# Copy code
# Example of an adjacency list representation for a graph with 4 vertices
# Adjacency List for a directed graph
# 0 -> [1]
# 1 -> [2, 3]
# 2 -> [0, 3]
# 3 -> []

def create_adj_list(num_vertices, edges):
    adj_list = [[] for _ in range(num_vertices)]
    for u, v in edges:
        adj_list[u].append(v)
    return adj_list

num_vertices = 4
edges = [(0, 1), (1, 2), (1, 3), (2, 0), (2, 3)]
print(create_adj_list(num_vertices, edges))



# 2. Breadth-First Search (BFS)
# python
# Copy code
from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    result = []
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    
    return result

# Example usage with an adjacency list
graph = create_adj_list(4, [(0, 1), (1, 2), (1, 3), (2, 0), (2, 3)])
print(bfs(graph, 0))  # Output: [0, 1, 2, 3]
3. Depth-First Search (DFS)
python
Copy code
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    result = [start]
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            result.extend(dfs(graph, neighbor, visited))
    
    return result

# Example usage with an adjacency list
graph = create_adj_list(4, [(0, 1), (1, 2), (1, 3), (2, 0), (2, 3)])
print(dfs(graph, 0))  # Output: [0, 1, 2, 3]



# 4. Dijkstra’s Algorithm
# python
# Copy code
import heapq

def dijkstra(graph, start):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices
    distances[start] = 0
    priority_queue = [(0, start)]  # (distance, vertex)
    
    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)
        
        if current_distance > distances[u]:
            continue
        
        for neighbor, weight in graph[u]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example usage with a weighted adjacency list
# Adjacency List: vertex -> [(neighbor, weight), ...]
graph = {
    0: [(1, 1), (2, 4)],
    1: [(2, 2), (3, 6)],
    2: [(3, 3)],
    3: []
}
print(dijkstra(graph, 0))  # Output: [0, 1, 3, 4]



# 5. Floyd-Warshall Algorithm
# python
# Copy code
def floyd_warshall(graph):
    num_vertices = len(graph)
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
    for u in range(num_vertices):
        dist[u][u] = 0
        for v, weight in graph[u]:
            dist[u][v] = weight
    
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# Example usage with a weighted adjacency matrix
# Adjacency Matrix: dist[i][j] represents the weight from i to j
graph = {
    0: [(1, 3), (2, 8), (3, float('inf'))],
    1: [(0, float('inf')), (2, 4), (3, 6)],
    2: [(0, float('inf')), (1, float('inf')), (3, 1)],
    3: [(0, float('inf')), (1, float('inf')), (2, float('inf'))]
}
print(floyd_warshall(graph))



# 6. Practice Problems
# Shortest Path in a Grid with Obstacles Elimination

# python
# Copy code
from collections import deque

def shortest_path_with_obstacles(grid, k):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 0, k)])  # (row, col, distance, remaining_obstacles)
    visited = set()
    
    while queue:
        r, c, dist, rem_obstacles = queue.popleft()
        if (r, c) == (rows - 1, cols - 1):
            return dist
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_rem_obstacles = rem_obstacles - grid[nr][nc]
                if new_rem_obstacles >= 0 and (nr, nc, new_rem_obstacles) not in visited:
                    visited.add((nr, nc, new_rem_obstacles))
                    queue.append((nr, nc, dist + 1, new_rem_obstacles))
    
    return -1

# Example usage with a grid and k
grid = [
    [0, 1, 1],
    [1, 0, 0],
    [1, 0, 0]
]
k = 1
print(shortest_path_with_obstacles(grid, k))  # Output: 4

# Number of Islands

# python
# Copy code
def num_islands(grid):
    def dfs(r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid) or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Mark as visited
        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            dfs(r + dr, c + dc)
    
    if not grid:
        return 0
    
    num_islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                num_islands += 1
                dfs(r, c)
    
    return num_islands

# Example usage with a grid
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]
print(num_islands(grid))  # Output: 3
