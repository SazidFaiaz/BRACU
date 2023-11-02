filein = open("input02.txt" , "r")
fileout = open("output02.txt" , "w")
x = int(filein.readline())
arr =[int(i) for i in filein.readline().strip().split(' ')]
print(arr)

def findMax(arr):
    if len(arr) == 1:
        return (arr[0])
    else:
        mid = len(arr) // 2
        left_max = findMax(arr[:mid])
        right_max = findMax(arr[mid:])
        return max(left_max, right_max)


max_value = findMax(arr)
print("Maximum value is:", max_value)
fileout.write(str(max_value))