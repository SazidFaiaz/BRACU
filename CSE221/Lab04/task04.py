f = open("input04.txt", 'r')
f_output = open("output04.txt", "w")
v, e = [int(i) for i in f.readline().strip().split(" ")]

adj = {}
for i in range(v + 1):
    adj[i] = []

for i in range(e):
    lst2 = f.readline().strip().split()
    x = int(lst2[0])
    y = int(lst2[1])
    adj[x].append(y)
f.close()

visited = (v + 1) * [False]
in_stack = (v + 1) * [False]
check = False


def dfs(G, u=1):
    visited[u] = True
    in_stack[u] = True
    for i in G[u]:
        if in_stack[i]:
            global check
            check = True
        if not visited[i]:
            dfs(G, i)
    in_stack[u] = False


dfs(adj)
if check:
    f_output.write("Yess")
else:
    f_output.write("NO")