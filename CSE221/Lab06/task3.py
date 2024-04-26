def getParent(parent, n):
    par = parent[n]
    if par==n:
        return par
    else:
        return getParent(parent, par)

f1 = open("input3.txt", "r")
f2 = open("output3.txt", "w")

inp = f1.read().split("\n")
f1.close()

config = inp[0].split(" ")
n = int(config[0])
k = int(config[1])

parent = [i for i in range(n + 1)]
friends = [1]*(n+1)

for i in range(1, len(inp),1):
    data = inp[i].split(" ")
    node1 = int(data[0])
    node2 = int(data[1])

    parent1 = getParent(parent, node1)
    parent2 = getParent(parent, node2)

    if (parent1!=parent2):
        parent[node2] = parent1
        parent[parent2] = parent1
        friends[parent1]= friends[parent1]+friends[parent2]
    f2.write(str(friends[parent1]))
    if i<len(inp)-1:
       f2.write("\n")
f2.close()

# Explanation:
# We have a getParent function that recursively finds the
# parent of all nodes. Initially, the parent of each node
# is themselves: We iterate through every connection and
# first get both node's parents. If their parents are different,
# it means they aren't friends. so, we set the parent of node 1
# to the parent of node 2, and also nade 2. we have also hept a
# list for friends of all nodes, so, friends of parent 1 will be
# incremented by friends of parents, The output is parent 1's
# friends at every step.

