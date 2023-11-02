
filein = open("input04.txt", "r")
fileout = open("output04.txt", "w")
x = int(filein.readline())
arr =[int(i) for i in filein.readline().strip().split(' ')]
print(arr)

def findMax(arr):
    if len(arr) == 1:
        return (arr[0])**2
    else:
        mid = len(arr) // 2
        left_max = findMax(arr[:mid])
        right_max = findMax(arr[mid:])
        return max(left_max, right_max)
Max = 0
for j in range(len(arr)-1):
    a = arr[j]
    b = findMax(arr[j+1:])
    m = a + b
    if m > Max:
        Max = m
print(Max)
fileout.write(f'This is output: {Max}')