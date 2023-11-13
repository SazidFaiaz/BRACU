from collections import deque
q = deque()
f = open("input05.txt", 'r')
f_output = open("output05.txt", "w")
v, e, d = [int(i) for i in f.readline().strip().split(" ")]

adj = {}
for i in range(v+1):
    adj[i] = []

for i in range(e):
    lst2 = f.readline().strip().split()
    x = int(lst2[0])
    y = int(lst2[1])
    adj[x].append(y)
    adj[y].append(x)
f.close()

visited = (v+1)*[False]
visited[1] = True
path = []
pre_city = [-1 for i in range(v+1)]


q.append(1)
path.append(1)
while len(q)!=0:
    u = q.popleft()
    for i in adj[u]:
        if visited[i]==False:
            visited[i] = True
            path.append(i)
            pre_city[i] = u
            q.append(i)

ans = []
k = d
count = -1
while k!=-1:
	ans.append(k)
	k = pre_city[k]
	count += 1

ans = ans[::-1]


f_output.write(f"Time: {count}\nShortest Path: ")
for i in ans:
    f_output.write(f"{i}, ")