#task05
filein = open("input05.txt", "r")
fileout = open("output05.txt", "w")
x = int(filein.readline())
arr =[int(i) for i in filein.readline().strip().split(' ')]
print(arr)

def quick_sort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quick_sort(arr, p, q - 1)
        quick_sort(arr, q + 1, r)

def partition(arr, p, r):
    x = arr[r]
    i = p - 1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

quick_sort(arr, 0, x - 1)

fileout.write(f"Output{arr}")