#22101309_Md.Sazid Faiaz sec04

import heapq
def read_file(filepath):
    g_str, heu_map = {}, {}

    with open(filepath, "r") as f:
        for line in f:
            ele = line.strip().split()
            if len(ele) < 2:
                continue

            node, heu = ele[0], int(ele[1])
            heu_map[node] = heu
            g_str[node] = [(ele[i], int(ele[i + 1])) for i in range(2, len(ele), 2)]

    return g_str, heu_map


def astar_algo(graph, heu, src, desti):
    if src not in graph or desti not in graph:
        return None, None

    pqueue = [(heu[src], src)]
    parent_d = {src: None}
    cost_d = {src: 0}

    while pqueue:
        pqueue.sort()  #lowest cost node processed first
        _, current = pqueue.pop(0)

        if current == desti:
            return trace_path(parent_d, src, desti), cost_d[desti]

        for neighbor, cost in graph[current]:
            new_cost = cost_d[current] + cost

            if neighbor not in cost_d or new_cost < cost_d[neighbor]:
                cost_d[neighbor] = new_cost
                parent_d[neighbor] = current
                pqueue.append((new_cost + heu[neighbor], neighbor))

    return None, None


def trace_path(p_map, start, end):
    route = []
    node = end
    while node:
        route.insert(0, node)
        node = p_map[node]
    return route


def output(path, dis):
    if path:
        print(f"Best Route: {' -> '.join(path)}")
        print(f"Total distance: {dis} km")
    else:
        print("Path Not Found")


if __name__ == "__main__":
    g_data, heu_data = read_file("input.txt")
    st = input("Start node: ")
    end = input("Destination: ")

    path, des_r = astar_algo(g_data, heu_data, st, end)
    output(path, des_r)
