from collections import defaultdict

def DFS(graph, start):
    # Initialize colors
    colors = defaultdict(int)

    dfs_path = []

    def explore(vertex):
        colors[vertex] = 1
        dfs_path.append(vertex)

        for neighbor in graph[vertex]:
            if colors[neighbor] == 0: # for recursive function
                explore(neighbor)

    explore(start)

    return dfs_path


with open('input03.txt', 'r') as file:
    lines = file.readlines()

N, M = map(int, lines[0].split())
roads = [list(map(int, line.split())) for line in lines[1:]]


graph = defaultdict(list)
for road in roads:
    u, v = road
    graph[u].append(v)
    graph[v].append(u)

dfs_path = DFS(graph, 1)
print(" ".join(map(str, dfs_path)))


with open('output03.txt', 'w') as output_file:
    output_file.write(" ".join(map(str, dfs_path)))
