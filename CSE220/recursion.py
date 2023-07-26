

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
