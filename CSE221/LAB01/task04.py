
fileIn = open("task4_Input.txt", mode='r')
outputFile = open('task4_Output.txt', mode='w')

line = fileIn.readlines()
n = int(line[0])
schedule = []

for i in line[1:]:
    parts = i.split()
    train_name = ' '.join(parts[:-5])
    departure_time = parts[-3]

    schedule.append((train_name, departure_time))

schedule.sort(key=lambda x: (x[0], -x[1], n - schedule.index(x)))

for schedule in schedule:
    outputFile.write(f'{schedule[0]} will departure for {schedule[1]}\n')

