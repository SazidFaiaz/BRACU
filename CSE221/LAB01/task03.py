
fileIn = open("Input1Task03.txt", mode='r')
outputFile = open('output01task03.txt', mode='w')
elem = fileIn.readline()
allelem = fileIn.readlines()
index = allelem[0].strip("\n")
marks = allelem[1].strip("\n")
print(index)
print(marks)
splitindex = index.split(" ")
splimarks = marks.split(" ")
splitindex = [int(x) for x in splitindex]
splimarks = [int(y) for y in splimarks]
students = [(splitindex[i], splimarks[i]) for i in range(int(elem))]
print(splitindex)
print(splimarks)
# def custom_sort(student):
#     return (-student[1], -student[0])
#
# # Sort the list using the custom sorting function
# students.sort(key=custom_sort)

students.sort(key=lambda x: (-x[1], x[0]))

for student in students:
    print(f'ID: {student[0]} Mark: {student[1]}')
    outputFile.write(f'ID: {student[0]} Mark: {student[1]}\n')