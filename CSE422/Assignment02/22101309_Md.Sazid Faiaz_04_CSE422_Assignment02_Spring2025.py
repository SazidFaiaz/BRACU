#22101309 Md.Sazid Faiaz

import random

num_of_gen = 1
cors_count , slot_count = 0 , 0
cors_data = []

def readinput(file_path):
    global cors_count, slot_count, cors_data
    with open(file_path, 'r') as file:
        first_line = file.readline().strip().split(' ')
        cors_count = int(first_line[0])
        slot_count = int(first_line[1])
        cors_data = []
        for line in file.readlines():
            cors_data.append(line.strip())

def chromo_str(chromo):
    return ''.join(str(bit) for slot in chromo for bit in slot)

def str_list(chromo_str):
    idx = 0
    chromo_list = []
    for i in range(slot_count):
        temp = []
        for j in range(cors_count):
            temp.append(int(chromo_str[idx]))
            idx += 1
        chromo_list.append(temp)
    return chromo_list

def populate(size=10):
    population = []
    i = 0
    while i < size:
        chrom = []
        j = 0

        while j < slot_count:
            chrom.append([random.choice((0, 1)) for _ in range(cors_count)])
            j += 1
        population.append(chrom)
        i += 1

    return population

def fitness(chromo):
    def overlap_penalty(chromo):
        penalty = 0
        for slot in chromo:
            overlap = sum(slot)
            penalty += max(0, overlap - 1)
        return penalty
    def consistency_penalty(chromo):
        penalty = 0
        course_idx = 0
        while course_idx < cors_count:
            count = 0
            slot_idx = 0

            while slot_idx < len(chromo):
                count += chromo[slot_idx][course_idx]
                slot_idx += 1

            penalty += abs(count - 1)
            course_idx += 1

        return penalty

    return -1 * (overlap_penalty(chromo) + consistency_penalty(chromo))


def mutate(chromo):
    r_slot = random.randrange(slot_count)
    r_course = random.randrange(cors_count)

    chromo[r_slot][r_course] = 1 - chromo[r_slot][r_course]

    return chromo

def select_parents(pop_size, selected_pairs):

    while True:
        p1, p2 = random.sample(range(pop_size), 2)

        if (p1, p2) not in selected_pairs and (p2, p1) not in selected_pairs:
            selected_pairs.add((p1, p2))
            return p1, p2

def encode(chrom):
    return ''.join(map(str, chrom))

def decode(chrom_str):
    return [int(bit) for bit in chrom_str]

def one_point_crossover(p1, p2):
    str1, str2 = encode(p1), encode(p2)
    point = random.randint(1, len(str1) - 1)

    ofsprng1 = decode(str1[:point] + str2[point:])
    ofsprng2 = decode(str2[:point] + str1[point:])

    return ofsprng1, ofsprng2

def multi_point_crossover(p1, p2):
    str1, str2 = encode(p1), encode(p2)
    pt1, pt2 = sorted(random.sample(range(1, len(str1) - 1), 2))

    print(f"Crossing between indices {pt1} and {pt2}")

    child1 = decode(str1[:pt1] + str2[pt1:pt2] + str1[pt2:])
    child2 = decode(str2[:pt1] + str1[pt1:pt2] + str2[pt2:])

    return child1, child2


# Genetic Algorithm
def genetic_solver(population, max_generations=100):
    global gen_count
    gen_count = 0

    while gen_count < max_generations:
        ranked = sorted(population, key=lambda c: fitness(c), reverse=True)

        if fitness(ranked[0]) == 0:
            return ranked[0]

        # Select top-performing candidates
        population = random.choices(ranked[:10], k=10)

        selected_pairs = []
        offspring = []

        for _ in range(5):
            parent1_idx, parent2_idx = select_parents(len(population), selected_pairs)
            child1, child2 = one_point_crossover(population[parent1_idx], population[parent2_idx])

            # Apply mutation with 30% probability
            if random.random() < 0.3:
                child1 = mutate(child1)
            if random.random() < 0.3:
                child2 = mutate(child2)

            offspring.extend([child1, child2])

        population = offspring
        gen_count += 1

    return sorted(population, key=lambda c: fitness(c), reverse=True)[0]


# Main function
def main():
    readinput("input.txt")
    population = populate()
    best = genetic_solver(population)

    print(f"Best chromosome: {encode(best)}")
    print(f"Best fitness: {fitness(best)}")


if __name__ == "__main__":
    main()

#part2
def experiment(population):
    idx1, idx2 = random.sample(range(len(population)), 2)
    child1, child2 = multi_point_crossover(population[idx1], population[idx2])

    print("Selected Parents:")
    print(f"Parent 1: {encode(population[idx1])}")
    print(f"Parent 2: {encode(population[idx2])}")

    print("Generated Offspring:")
    print(f"Child 1: {encode(child1)}")
    print(f"Child 2: {encode(child2)}")


if __name__ == "__main__":
    readinput("input.txt")
    population = populate()
    experiment(population)
