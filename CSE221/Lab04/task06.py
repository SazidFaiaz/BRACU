# f = open("input06.txt", 'r')
# f_out = open("output06.txt", "w")
# v, e = [int(i) for i in f.readline().strip().split(" ")]
# adj = [[0 for i in range(e)] for i in range(v)]
#
# ab = f.read().strip().split("\n")
# visited = [[False for i in range(e)] for j in range(v)]
#
# for i in range(len(ab)):
# 	for j in range(len(ab[i])):
# 		adj[i][j] = ab[i][j]
#
#
#
# def check_valid(adj, i, j):
# 	global visited
# 	global v
# 	global e
#
# 	if i<0:
# 		return False
#
# 	if i>=v:
# 		return False
#
# 	if j<0:
# 		return False
#
# 	if j>=e:
# 		return False
#
# 	if visited[i][j]:
# 		return False
#
# 	if adj[i][j]=="#":
# 		return False
#
# 	if adj[i][j]=="." or adj[i][j]=="D":
# 		visited[i][j] = True
# 		return True
#
# def dfs(adj, x, y):
# 	if not check_valid(adj, x, y):
# 		return 0
#
# 	else:
# 		dmd = 0
# 		if adj[x][y]=="D":
# 			dmd += 1
#
# 		dmd += dfs(adj, x-1, y)
# 		dmd += dfs(adj, x+1, y)
# 		dmd += dfs(adj, x, y+1)
# 		dmd += dfs(adj, x, y-1)
#
# 		return dmd
#
#
# max_dmd = 0
# for i in range(v):
#     for j in range(e):
#         if adj[i][j] == '.' and not visited[i][j]:
#             dmd = dfs(adj, i, j)
#             max_dmd = max(max_dmd, dmd)
#
# f_out.write(str(max_dmd))

file_in = open('input06.txt', 'r')
file_out = open('output06.txt', 'w')
temp = file_in.readline().split(' ')
row, col = int(temp[0]), int(temp[1])
grid = [[] for i in range(row)]
queue = []
visited = [[0] * col for i in range(row)]
maximum = 0

for i in range(row):
	temp = file_in.readline()
	for j in temp:
		if j != '\n':
			grid[i].append(j)
	print(grid)


def diamond(grid, visited, r, c):
	dim = 0
	if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or visited[r][c] > 0 or grid[r][c] == '#':
		return 0
	visited[r][c] = 1

	if grid[r][c] == 'D':
		dim += 1
	dim += diamond(grid, visited, r + 1, c)
	dim += diamond(grid, visited, r - 1, c)
	dim += diamond(grid, visited, r, c + 1)
	dim += diamond(grid, visited, r, c - 1)
	return dim


for i in range(row):
	for j in range(col):
		if grid[i][j] == '.':
			result = diamond(grid, visited, i, j)
			maximum = max(result, maximum)

file_out.write(f'{maximum}')
file_out.close()