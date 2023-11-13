from collections import defaultdict

def DFS(graph, start):
    # Initialize colors
    colors = defaultdict(int)

    # List to store the DFS path
    dfs_path = []

    def explore(vertex):
        colors[vertex] = 1
        dfs_path.append(vertex)

        for neighbor in graph[vertex]:
            if colors[neighbor] == 0:
                explore(neighbor)

    # Start DFS from the given start vertex
    explore(start)

    return dfs_path

# Input from a text file
with open('input03.txt', 'r') as file:
    lines = file.readlines()

N, M = map(int, lines[0].split())
roads = [list(map(int, line.split())) for line in lines[1:]]

# Create an adjacency list representation of the graph
graph = defaultdict(list)
for road in roads:
    u, v = road
    graph[u].append(v)
    graph[v].append(u)

# Find and print the DFS traversal path
dfs_path = DFS(graph, 1)
print(" ".join(map(str, dfs_path)))

# Write the DFS path to an output file
with open('output03.txt', 'w') as output_file:
    output_file.write(" ".join(map(str, dfs_path)))
