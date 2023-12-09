def getParent(parent, n):
    par = parent[n]
    if par == n:
        return par
    else:
        return getParent(parent, par)


f1 = open("input4.txt", "r")
f2 = open("output4.txt", "w")

inp = f1.read().split("\n")
f1.close()
line1 = inp[0].split(" ")
nodes = int(line1[0])
edges = int(line1[1])

conn = []
graph = []
parent = [0] * (nodes + 1)
totalCost = 0

parent = [i for i in range(nodes + 1)]

for i in range(1, len(inp) - 1, 1):
    info = inp[i].split(" ")
    node1 = int(info[0])
    node2 = int(info[1])
    cost = int(info[2])
    lst = [node1, node2, cost]
    conn.append(lst)

conn = sorted(conn, key=lambda x: x[2])

for i in range(len(conn)):
    node1 = conn[i][0]
    node2 = conn[i][1]
    cost = conn[i][2]

    parent1 = getParent(parent, node1)
    parent2 = getParent(parent, node2)

    if (parent1 != parent2):
        parent[node2] = parent1
        parent[parent2] = parent1
        graph.append(conn[i])
        totalCost += cost

f2.write(str(totalCost))
f2.close()

# Here, we have to find the minimum First, the vertices are sorted spanning
# tree cost. in ascending order of cost. Then, we have to
# iterate through this lif list of sorted vertices. For the
# two nodes in every connection, we find their parents:

# This is done by calling the function
# 'getponent' that recursively finds the parent of the node.
# It the two ponents are different, this means that they
# The two nodes can be joined as there is no fean of
# cycle. So, we set the ponent of node 2 as ponent 1 and
# parent of the node 2's parent as ponent I. Then, we
# append this vertice to the graph and add the cost to
# a totalcost voniable. After the loop ends, the result
# is this total Cost.