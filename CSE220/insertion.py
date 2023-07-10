#Insertion

def insert(arr , index , value):

    for i in range(len(arr)-1 , index, -1):
        arr[i] = arr[i -1]

    arr[index] = value

    print(arr)


arr = [1,2,3,4,5,None]
insert(arr, 2, 0)
