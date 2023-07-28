
def fact(n):
    if n == 0 or n == 1:
        return n  #base function
    else:
        return n * fact(n-1)

#find the sum of numbers of a linked list iteratively
# def interativesum(head):
#     sum = 0
#     temp = head
#     while temp:
#         sum += temp.element
#         temp = temp.next
#     return sum
# recursive solution of this code:

def recursivesm(head):
    if head.next == None:
        return head.element # Base case
    else:
        return head.element+recursivesm(head.next) # recursive part

#Length of a String

def strlength(str):
    if len(str) == 0:
        return 0
    else:
        return 1+strlength(str[1:])

#Length of a linked list:

def lenLinkedlist(head):
    if head == None:
        return 0
    else:
        return 1+lenLinkedlist(head.next)

#Sequential search in a sequence:

def sequnsearch(head,key):
    if head == None:
        return False
    elif head.element == key:
        return True
    else:
        return sequnsearch(head.next, key) #recursive

def seqsearch(arrar,key):
    if len(arrar) == 0:
        return False
    elif arrar[0] == key:
        return True
    else:
        return seqsearch(arrar[1:],key) #recursive

def contains(arr, left, key):
    if left >= len(arr):
        return False
    elif arr[left] == key:
        return True
    else:
        return contains(arr,left+1,key)

#Binary search in a sorted array:

def contain(arr, left, right, key):
    if left > right:
        return False #base case
    else:
        mid = (left+right)//2
        if key == arr[mid]:
            return True
        elif key > arr[mid]:
            return contain(arr, mid + 1, right, key)
        else:
            return contain(arr, left, mid-1, key)
#Finding the maximum in a sequence
def maximum(a,b):
    return a if a >= b else b

def findMax(head):
    if head.next == None:
        return head.element
    else:
        newmax = findMax(head.next)
        return maximum(head.element, newmax)
# for array
def arrayMax(arr, left):
    if left == len(arr)-1:
        return arr[left]
    else:
        maxreset = arrayMax(arr, left+1)
        return maximum(arr[left], maxreset)

#Finding the maximum in an array
def max(arr, left, right):
    if left == right:
        return arr[left]
    else:
        mid = (left + right)//2
        maxlefthalf = max(arr, left, mid)
        maxrighthalf = max(arr, mid+1, right)
        return maximum(maxlefthalf, maxrighthalf)


