
fileIn = open("input2.txt", mode='r')

n = int(fileIn.readline())
arr = list(map(int, fileIn.readline().split()))

def bubbleSort(arr):
    swapped = True

    for i in range(len(arr) - 1):
        swapped = False

        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:

                arr[j], arr[j + 1] = arr[j + 1], arr[j]

                swapped = True

        if not swapped:
            break
bubbleSort(arr)

with open('output2.txt', 'w') as f:
    f.write(' '.join(map(str, arr)))