f = open("input06.txt", 'r')
f_out = open("output06.txt", "w")
v, e = [int(i) for i in f.readline().strip().split(" ")]
adj = [[0 for i in range(e)] for i in range(v)]

ab = f.read().strip().split("\n")
visited = [[False for i in range(e)] for j in range(v)]

for i in range(len(ab)):
	for j in range(len(ab[i])):
		adj[i][j] = ab[i][j]



def check_valid(adj, i, j):
	global visited
	global v
	global e

	if i<0:
		return False

	if i>=v:
		return False

	if j<0:
		return False

	if j>=e:
		return False

	if visited[i][j]:
		return False

	if adj[i][j]=="#":
		return False

	if adj[i][j]=="." or adj[i][j]=="D":
		visited[i][j] = True
		return True

def dfs(adj, x, y):
	if not check_valid(adj, x, y):
		return 0

	else:
		dmd = 0
		if adj[x][y]=="D":
			dmd += 1

		dmd += dfs(adj, x-1, y)
		dmd += dfs(adj, x+1, y)
		dmd += dfs(adj, x, y+1)
		dmd += dfs(adj, x, y-1)

		return dmd


max_dmd = 0
for i in range(v):
    for j in range(e):
        if adj[i][j] == '.' and not visited[i][j]:
            dmd = dfs(adj, i, j)
            max_dmd = max(max_dmd, dmd)

f_out.write(str(max_dmd))

