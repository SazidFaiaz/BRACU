from collections import defaultdict, deque
#Q1
def read_input(filepath):
    with open(filepath, "r") as file:
        lines = file.readlines()
        n, m = map(int, lines[0].split())
        edges = [line.strip() for line in lines[1:-1]]
        start_city = lines[-1].strip()
    return n, m, edges, start_city
#Q2
def create_adj_list(edges):
    adj_list = defaultdict(list)
    for edge in edges:
        u, v = edge.split("*")
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list

#Q3
def bfs(adj_list, start_city):
    distance = {city: float("inf") for city in adj_list}
    distance[start_city] = 0
    queue = deque([start_city])

    while queue:
        current_city = queue.popleft()
        for neighobor in adj_list[current_city]:
            if distance[neighobor] == float("inf"):
                distance[neighobor] = distance[current_city]+1
                queue.append(neighobor)
    return distance

def cat_city(distance, start_city):
    today_deli = [city for city, distance in distance.items() if distance % 2 == 1 and city != start_city]
    tomorrow_deli = [city for city, distance in distance.items() if distance % 2 == 0 and city != start_city]
    return today_deli, tomorrow_deli

def write_out(output_file, today_deli, tomorrow_deli):
    with open(output_file, "w") as file:
        file.write("Today's delivery: {}\n".format(','.join(sorted(today_deli))))
        file.write("Today's delivery: {}\n".format(','.join(sorted(tomorrow_deli))))



    input_file_path = "input1.txt"
    output_file_path = "output1.txt"

    n, m, edges, start_city = read_input(input_file_path)
    adj_list = create_adj_list(edges)
    today_deli, tomorrow_deli = cat_city(distance, start_city)
    write_out(output_file_path, today_deli, tomorrow_deli)


#Q4
def read_input(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        n, m = map(int, lines[0].split())
        edges = [line.strip() for line in lines[1:-1]]
        start_city = lines[-1].strip()
    return n, m, edges, start_city

def create_adjacency_list(edges):
    adjacency_list = defaultdict(list)
    for edge in edges:
        u, v = edge.split('*')
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
    return adjacency_list

def remove_inaccessible_cities(adjacency_list, inaccessible_cities):
    for city in inaccessible_cities:
        del adjacency_list[city]
        for neighbor, neighbors_list in adjacency_list.items():
            adjacency_list[neighbor] = [n for n in neighbors_list if n != city]
    return adjacency_list

def bfs(adjacency_list, start_city):
    distances = {city: float('inf') for city in adjacency_list}
    distances[start_city] = 0
    queue = deque([start_city])

    while queue:
        current_city = queue.popleft()
        for neighbor in adjacency_list[current_city]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current_city] + 1
                queue.append(neighbor)

    return distances

def categorize_cities(distances, start_city):
    today_delivery = [city for city, distance in distances.items() if distance % 2 == 1 and city != start_city]
    tomorrow_delivery = [city for city, distance in distances.items() if distance % 2 == 0 and city != start_city]
    return today_delivery, tomorrow_delivery

def write_output(output_file, today_delivery, tomorrow_delivery):
    with open(output_file, 'w') as file:
        file.write("Today's delivery: {}\n".format(','.join(sorted(today_delivery))))
        file.write("Tomorrow's delivery: {}\n".format(','.join(sorted(tomorrow_delivery))))

if __name__ == "__main__":
    input_file_path = "input2.txt"
    output_file_path = "output2.txt"

    n, m, edges, start_city = read_input(input_file_path)
    adjacency_list = create_adjacency_list(edges)

    inaccessible_cities = ['d', 'g', 'k']

    adjacency_list = remove_inaccessible_cities(adjacency_list, inaccessible_cities)

    distances = bfs(adjacency_list, start_city)
    today_delivery, tomorrow_delivery = categorize_cities(distances, start_city)
    write_output(output_file_path, today_delivery, tomorrow_delivery)
