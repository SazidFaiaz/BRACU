filein = open("input03.txt", "r")
fileout = open("output03.txt", "w")
x = int(filein.readline())
arr =[int(i) for i in filein.readline().strip().split(' ')]
# print(arr)

def mergeSort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left_half, count_left = mergeSort(arr[:mid])
    right_half, count_right = mergeSort(arr[mid:])
    merged, count = merge(left_half, right_half)
    return merged, (count_left+count_right+count)

def merge(a, b):
    merged = []
    count = 0
    i = j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1 # smallest value add i
        else:
            merged.append(b[j]) # biggest value add j
            j += 1
            count += len(a) - i

    # Add the remaining elements from both lists (if any)
    while i < len(a):
        merged.append(a[i])
        i += 1

    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged, count


_, count = mergeSort(arr)
print("Sorted array is:", count)
fileout.write(f'This is output: {count}')