#6
import sys
sys.setrecursionlimit(1000000)
filein = open("input06.txt", "r")
fileout = open("output06.txt", "w")
x = int(filein.readline())
# print(x)
arr =[int(i) for i in filein.readline().strip().split(' ')]
print(arr)
y = int(filein.readline())
print(y)
k = [int(j.strip('\n')) for j in filein.readlines()]
print(k)

def findK(arr, l, r, k):
    if k > 0 and k <= r - l + 1:

        q = partition(arr, l, r)

        if q-l == k-1:
            return arr[q]

        if q-l > k-1:
            return findK(arr, l, q-1, k)
        else:
            return findK(arr, q+1, r, k-q+l-1)

    else:
        print("out of bound")


def partition(arr, l, r):
    x = arr[r]
    i = l - 1
    for j in range(l, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

for i in range(y):
    print(findK(arr, 0, x-1, k[i]))
    fileout.write(f'{findK(arr, 0, x-1, k[i])}')