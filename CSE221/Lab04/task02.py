from collections import defaultdict, deque

def BFS(graph, start):
    # Initialize colors and queue
    colors = defaultdict(int)
    queue = deque()

    # Set the color of the start node to 1 (visited)
    colors[start] = 1
    queue.append(start)

    # List to store the BFS path
    bfs_path = []

    while queue:
        u = queue.popleft()
        bfs_path.append(u)

        for v in graph[u]:
            if colors[v] == 0:
                colors[v] = 1
                queue.append(v)

    return bfs_path

# Input from a text file
with open('input02.txt', 'r') as file:
    lines = file.readlines()

N, M = map(int, lines[0].split())
roads = [list(map(int, line.split())) for line in lines[1:]]

# Create an adjacency list representation of the graph
graph = defaultdict(list)
for road in roads:
    u, v = road
    graph[u].append(v)
    graph[v].append(u)

# Find and print the BFS traversal path
bfs_path = BFS(graph, 1)
print(" ".join(map(str, bfs_path)))

with open('output02.txt', 'w') as file:
    file.write(" ".join(map(str, bfs_path)))