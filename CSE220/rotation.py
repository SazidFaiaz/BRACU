#left rotation k cell

def left_rotate(arr, k):
    for j in range(k):
        temp = arr[0]
        for i in range(1,len(arr)):
            arr[i-1] = arr[i]
        arr[len(arr)-1] = temp
    print(arr)

arr = [1,2,3,4,5]
k= 1
left_rotate(arr, k)

#right rotating

def right_rotate(arr , k):
    for i in range(k):
        temp = arr[len(arr)-1]
        for j in range(len(arr)-1,0,-1):
            arr[j] = arr[j-1]
        arr[0] =temp
    print(arr)

arr = [10,20,30,40,50]
k = 1
right_rotate(arr, k)