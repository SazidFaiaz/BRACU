from collections import defaultdict

filein = open("input01B.txt", "r")
fileout = open("output01B.txt", "w")

N, M = map(int, filein.readline().split())
# print(N, M)

adj_list = defaultdict(list)

for i in range(M):
    u, v, w = map(int, filein.readline().strip().split(" "))
    # print(u, v, w)
    adj_list[u].append((v, w))


def print_adj_list(adj_list):
    for vertex in range(1, max(adj_list.keys()) + 1):
        neighbors = adj_list[vertex]
        neighbors_str = " ".join([f"({v},{w})" for v, w in neighbors])
        print(f"{vertex} : {neighbors_str}")
        fileout.write(f"{vertex} : {neighbors_str}\n")


print_adj_list(adj_list)

