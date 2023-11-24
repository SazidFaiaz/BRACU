filein = open("input01.txt", "r")
fileout = open("output01.txt", "w")
x = int(filein.readline())
arr =[int(i) for i in filein.readline().strip().split(' ')]
print(arr)

def merge(a, b):
    merged = []
    i = j = 0 # etarate two array

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1

    # Add the remaining elements from both lists (if any)
    while i < len(a):
        merged.append(a[i])
        i += 1

    while j < len(b): # 2nd rray
        merged.append(b[j])
        j += 1

    return merged

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        left_half = mergeSort(left_half)
        right_half = mergeSort(right_half)
        return merge(left_half, right_half)

# arr = [9, 5, 4, 6, 1, 3, 2, 9]
sorted_arr = mergeSort(arr)
print("Sorted array is:", sorted_arr)
fileout.write(f'This is output{sorted_arr}')